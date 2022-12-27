from fastapi import FastAPI
from db import get_db_connection
from models import ClientOrder
from utils import TradeBook
from typing import Dict
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime

app = FastAPI(title='TRADE_BOOK', version='1.0')

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True)


@app.get('/')
def trade_history() -> Dict:
    connection, cursor = get_db_connection()
    # Load the initial positions and prices from the database
    cursor.execute("SELECT * FROM trade_history")
    history = cursor.fetchall()
    return {"message": 'Welcome to the trade book.', 'History': history}


@app.post("/trade")
def trade(order: ClientOrder) -> Dict:
    connection, cursor = get_db_connection()

    # Load the initial positions and prices from the database
    cursor.execute("SELECT * FROM positions")
    initial_positions = {row[0]: row[1] for row in cursor.fetchall()}
    cursor.execute("SELECT * FROM prices")
    market_prices = {row[0]: row[1] for row in cursor.fetchall()}

    # Load the transaction costs, risk aversion, and volatilises from the database
    cursor.execute("SELECT * FROM transaction_costs")
    transaction_costs = {row[0]: row[1] for row in cursor.fetchall()}
    cursor.execute("SELECT * FROM risk_aversion")
    risk_appetite = cursor.fetchone()[0]
    cursor.execute("SELECT * FROM volatilities")
    volatility = {row[0]: row[1] for row in cursor.fetchall()}

    # Initialize the TradeBook with the initial positions and prices
    trade_book = TradeBook(initial_positions=initial_positions, initial_market_prices=market_prices,
                           volatility=volatility, risk_appetite=risk_appetite, transaction_costs=transaction_costs,
                           hedge=order.hedge)

    # Add the client order to the trade book
    trade_book.add_client_order(order.instrument_id, order.traded_price, order.quantity)

    # Update the positions and prices in the database
    for instrument_id, position in trade_book.positions.items():
        cursor.execute("UPDATE positions SET position = %s WHERE instrument_id = %s", (position, instrument_id))
    for instrument_id, price in trade_book.market_prices.items():
        cursor.execute("UPDATE prices SET price = %s WHERE instrument_id = %s", (price, instrument_id))

    timestamp = str(datetime.now())
    sharpe_ratio = trade_book.calculate_sharpe_ratio(risk_free_rate=0.03, time_period=1)
    roi = trade_book.calculate_roi(instrument_id=order.instrument_id)
    var = int(trade_book.calculate_var(alpha=0.95))
    calmar = trade_book.calculate_calmar_ratio(time_period=1)

    cursor.execute("INSERT INTO trade_history (instrument_id, position, timestamp, price) VALUES (%s, %s, %s, %s)",
                   (order.instrument_id, order.quantity, timestamp, order.traded_price))

    connection.commit()
    cursor.close()
    connection.close()

    return {'Instrument Traded': order.instrument_id, "P&L for the portfolio": trade_book.pnl,
            'Max Drawdown': trade_book.maximum_drawdown,
            'Hedged?': str(order.hedge), 'Price': str(order.traded_price),
            'Value at Risk': var,
            'sharpe_ratio': sharpe_ratio,
            'ROI': roi,
            'Calmar Ratio': calmar}

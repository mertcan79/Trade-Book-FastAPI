from fastapi import FastAPI
from db import get_db_connection
from models import ClientOrder
from utils import TradeBook
from typing import Dict
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title='TRADE_BOOK', version='1.0')

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True)


@app.get('/')
def home() -> Dict:
    connection, cursor = get_db_connection()
    # Load the initial positions and prices from the database
    cursor.execute("SELECT * FROM positions")
    initial_positions = {row[0]: row[1] for row in cursor.fetchall()}
    cursor.execute("SELECT * FROM prices")
    initial_market_prices = {row[0]: row[1] for row in cursor.fetchall()}

    return {"message": 'Welcome to the trade book.', 'Initial Market Prices': initial_market_prices,
            'Positions': initial_positions}


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

    connection.commit()
    cursor.close()
    connection.close()

    return {'instrument': order.instrument_id, "pnl": trade_book.pnl, 'Max Drawdown': trade_book.maximum_drawdown,
            'Hedged?': str(order.hedge), 'Price': order.traded_price,
            'Value at Risk': trade_book.calculate_var(alpha=0.95)
            }

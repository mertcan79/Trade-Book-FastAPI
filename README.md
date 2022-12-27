# FastAPI based Trade Book 

FastAPI based Trade Book implementation with multiple features like hedging, stop-loss, VaR calculation, P&L and Max Drawdown calculations.

When managing a trading book with instruments, initial positions and prices at the beginning of the day, you will trade with clients and the positions will be changed. 
A premium is charged from the clients so the traded price might not be the same as the market.

Classes are written for ClientOrder, MarketUpdate, TradeBook which deals with the trade activities and calculates real-time P&L.
They are initialized with the initial positions and initial market prices, and has four functions:

(a) add_client_order – with argument as an instance of ClientOrder
(b) update_market_price – with argument as an instance of MarketUpdate
(c) get_pnl – returns the accumulated Profit &amp; Loss (P&amp;L) from the start of the day
(d) get_maximum_drawdown – returns the maximum drawdown from the start of the day

Since the prices change rapidly during the day, instead of just holding your positions, one will liquidate the position in the market, but with some transaction cost for instrument as a fixed proportion of quantity.

Assuming the trades can be executed immediately after a client order, P&L and Max Drawdown are changed to reflect this strategy (with or without hedge).

It is assumed that the client order and hedge happen simultaneously, so P&L is not changed before and after the hedge. 

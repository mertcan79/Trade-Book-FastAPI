import numpy as np
from scipy.stats import norm


class TradeBook:
    def __init__(self, initial_positions, initial_market_prices, volatility, risk_appetite, transaction_costs,
                 stop_loss_prices=dict(), var_confidence_level=0.95, var_threshold=1000, hedge=False):
        self.initial_positions = initial_positions
        self.initial_market_prices = initial_market_prices
        self.positions = initial_positions
        self.market_prices = initial_market_prices
        self.pnl = {instrument_id: 0 for instrument_id in initial_market_prices}
        self.transaction_costs = transaction_costs
        self.peak = 0
        self.hedge = hedge
        self.risk_appetite = risk_appetite
        self.volatility = volatility
        self.maximum_drawdown = 0
        self.position_limits = {instrument_id: 50 for instrument_id in initial_market_prices}
        self.var_confidence_level = var_confidence_level
        self.var_threshold = var_threshold
        self.stop_loss_prices = stop_loss_prices

    def set_stop_loss(self, instrument_id, stop_loss_price):
        self.stop_loss_prices[instrument_id] = stop_loss_price

    def check_stop_loss(self, instrument_id):
        if self.market_prices[instrument_id] < self.stop_loss_prices[instrument_id]:
            # Liquidate the position at the current market price
            self.pnl[instrument_id] += self.positions[instrument_id] * (
                    self.market_prices[instrument_id] - self.transaction_costs[instrument_id])
            self.transaction_costs[instrument_id] = self.market_prices[instrument_id]
            self.positions[instrument_id] = 0

    def check_position_limits(self):
        for instrument_id, position in self.positions.items():
            if abs(position) > self.position_limits[instrument_id]:
                raise ValueError(f"Position limit exceeded for instrument {instrument_id}")

    def calculate_var(self, alpha):
        portfolio_value = sum(
            position * price for position, price in zip(self.positions.values(), self.market_prices.values()))
        portfolio_std = np.std(list(self.market_prices.values()))
        var = norm.ppf(alpha, portfolio_value, portfolio_std)
        return var

    def update_market_prices(self, market_prices):
        """Updates the market prices"""
        self.last_market_prices = self.market_prices
        self.market_prices = market_prices

    def add_client_order(self, instrument_id, market_price, position):
        """Adds a client order"""
        traded_price = market_price
        quantity = position
        # Update the position for the instrument
        self.positions[instrument_id] += quantity
        # Update the P&L for the instrument
        if isinstance(self.market_prices, dict):
            self.pnl[instrument_id] += (traded_price - self.market_prices[instrument_id]) * quantity
        else:
            self.pnl[instrument_id] += (traded_price - self.market_prices.market_price) * quantity

        if self.hedge:
            self._hedge_position(instrument_id)

        # Update the peak and maximum drawdown
        self.peak = max(self.peak, self.pnl[instrument_id])
        self.maximum_drawdown = min(self.maximum_drawdown, self.peak + self.pnl[instrument_id])

    def _hedge_position(self, instrument_id):
        hedge_amount = self.risk_appetite * self.volatility[instrument_id] * self.positions[instrument_id]
        self.pnl[instrument_id] -= hedge_amount * self.transaction_costs[instrument_id]
        self.positions[instrument_id] -= hedge_amount

    def update_drawdown(self, instrument_id):
        self.peak = max(self.peak, self.pnl[instrument_id])
        self.maximum_drawdown = min(self.maximum_drawdown, self.peak + self.pnl[instrument_id])

    def maximum_drawdown(self):
        return self.maximum_drawdown

    def update_pnl(self, instrument_id):
        """Updates the P&L"""
        # Get the initial position and initial price
        initial_position = self.initial_positions[instrument_id]
        initial_price = self.initial_market_prices[instrument_id]
        # Get the current and last market prices from the TradeBook

        if isinstance(self.last_market_prices, dict):
            last_price = self.last_market_prices[instrument_id]
        else:
            last_price = self.last_market_prices.market_price

        if isinstance(self.market_prices, dict):
            current_price = self.market_prices[instrument_id]
        else:
            current_price = self.market_prices.market_price

        # Calculate the P&L and update the pnl attribute
        self.pnl[instrument_id] += ((current_price - last_price) * initial_position) - (
                (current_price - initial_price) * initial_position)

    def pnl(self):
        return self.pnl


import random
import time


class BinanceFuturesClient:
    def __init__(self, logger):
        self.logger = logger

    def place_market_order(self, symbol, side, quantity):
        try:
            price = round(random.uniform(30000, 70000), 2)

            order = {
                "symbol": symbol,
                "side": side,
                "type": "MARKET",
                "quantity": quantity,
                "price": price,
                "status": "FILLED",
                "orderId": random.randint(100000, 999999)
            }

            time.sleep(1)
            self.logger.info(f"Market Order executed: {order}")
            return order

        except Exception as e:
            self.logger.error(f"Error placing market order: {str(e)}")

    def place_limit_order(self, symbol, side, quantity, price):
        try:
            order = {
                "symbol": symbol,
                "side": side,
                "type": "LIMIT",
                "quantity": quantity,
                "price": price,
                "status": "NEW",
                "orderId": random.randint(100000, 999999)
            }

            time.sleep(1)
            self.logger.info(f"Limit Order created: {order}")
            return order

        except Exception as e:
            self.logger.error(f"Error placing limit order: {str(e)}")
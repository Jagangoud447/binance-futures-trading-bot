import argparse
from logger import setup_logger
from binance_client import BinanceFuturesClient


def main():
    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")

    parser.add_argument("--symbol", required=True, help="Trading pair (e.g., BTCUSDT)")
    parser.add_argument("--side", required=True, choices=["BUY", "SELL"], help="Order side")
    parser.add_argument("--type", required=True, choices=["MARKET", "LIMIT"], help="Order type")
    parser.add_argument("--quantity", required=True, type=float, help="Order quantity")
    parser.add_argument("--price", type=float, help="Price (required for LIMIT orders)")

    args = parser.parse_args()

    logger = setup_logger()
    client = BinanceFuturesClient(logger)

    logger.info("Starting Binance Futures Bot...")

    if args.type == "MARKET":
        client.place_market_order(
            symbol=args.symbol,
            side=args.side,
            quantity=args.quantity
        )

    elif args.type == "LIMIT":
        if not args.price:
            logger.error("Price is required for LIMIT orders.")
            return

        client.place_limit_order(
            symbol=args.symbol,
            side=args.side,
            quantity=args.quantity,
            price=args.price
        )


if __name__ == "__main__":
    main()
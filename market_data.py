import ccxt.async_support as ccxt
import logging

logger = logging.getLogger(__name__)


class MarketData:
    def __init__(self):
        self.exchange = ccxt.binance({
            "enableRateLimit": True
        })

    async def get_price(self, symbol="BTC/USDT"):
        try:
            ticker = await self.exchange.fetch_ticker(symbol)

            return {
                "symbol": symbol,
                "price": ticker["last"],
                "status": "success"
            }

        except Exception:
            logger.exception("Failed to fetch market price")

            return {
                "symbol": symbol,
                "price": None,
                "status": "error"
            }

    async def get_candles(
        self,
        symbol="BTC/USDT",
        timeframe="1h",
        limit=100
    ):
        try:
            candles = await self.exchange.fetch_ohlcv(
                symbol,
                timeframe=timeframe,
                limit=limit
            )

            return candles

        except Exception:
            logger.exception("Failed to fetch candles")
            return []

    async def close(self):
        await self.exchange.close()

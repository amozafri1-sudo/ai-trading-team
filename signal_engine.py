from technical import TechnicalAnalysis


class SignalEngine:

    @staticmethod
    def generate(prices):
        if len(prices) < 20:
            return {
                "signal": "WAIT",
                "reason": "Not enough market data"
            }

        analysis = TechnicalAnalysis.analyze(prices)

        sma = analysis["sma"]
        rsi = analysis["rsi"]
        current_price = prices[-1]

        if sma is None or rsi is None:
            return {
                "signal": "WAIT",
                "reason": "Indicators unavailable"
            }

        if current_price > sma and rsi < 70:
            return {
                "signal": "LONG",
                "reason": "Price above SMA and RSI below 70"
            }

        if current_price < sma and rsi > 30:
            return {
                "signal": "SHORT",
                "reason": "Price below SMA and RSI above 30"
            }

        return {
            "signal": "WAIT",
            "reason": "No clear trading setup"
        }

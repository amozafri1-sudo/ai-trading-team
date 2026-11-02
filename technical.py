class TechnicalAnalysis:

    @staticmethod
    def calculate_sma(prices, period=20):
        if len(prices) < period:
            return None

        values = prices[-period:]
        return sum(values) / period

    @staticmethod
    def calculate_rsi(prices, period=14):
        if len(prices) <= period:
            return None

        gains = []
        losses = []

        for i in range(1, len(prices)):
            change = prices[i] - prices[i - 1]
            gains.append(max(change, 0))
            losses.append(max(-change, 0))

        avg_gain = sum(gains[-period:]) / period
        avg_loss = sum(losses[-period:]) / period

        if avg_loss == 0:
            return 100

        rs = avg_gain / avg_loss
        return 100 - (100 / (1 + rs))

    @staticmethod
    def analyze(prices):
        sma = TechnicalAnalysis.calculate_sma(prices)
        rsi = TechnicalAnalysis.calculate_rsi(prices)

        return {
            "sma": sma,
            "rsi": rsi
        }

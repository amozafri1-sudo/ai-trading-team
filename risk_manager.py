class RiskManager:

    def __init__(self, max_risk=0.01):
        self.max_risk = max_risk

    def calculate_position_size(
        self,
        balance,
        entry_price,
        stop_loss
    ):
        if balance <= 0 or entry_price <= 0:
            return 0

        risk_amount = balance * self.max_risk
        price_difference = abs(entry_price - stop_loss)

        if price_difference <= 0:
            return 0

        position_size = risk_amount / price_difference

        return position_size

    def check_risk_reward(
        self,
        entry_price,
        stop_loss,
        take_profit
    ):
        risk = abs(entry_price - stop_loss)
        reward = abs(take_profit - entry_price)

        if risk == 0:
            return False

        risk_reward = reward / risk

        return risk_reward >= 2

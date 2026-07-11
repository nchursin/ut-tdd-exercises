from app.company import Company
from app.price_provider import IPriceProvider


class Report:
    def __init__(self, shares, price_provider: IPriceProvider) -> None:
        self._shares = shares
        self._price_provider = price_provider

    def get_line(self, company: Company) -> dict:
        shares = self._shares[company]
        price = self._price_provider.get_current_price(company)
        return {
            "company": company.__str__(),
            "shares": shares.count(),
            "current_price": price.__str__(),
            "current_value": (price * shares.count()).__str__(),
            "last_operation": shares.last_operation().__str__(),
        }

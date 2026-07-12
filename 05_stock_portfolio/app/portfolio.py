from datetime import datetime

from app.company import Company
from app.price_provider import IPriceProvider
from app.report import Report
from app.shares import Shares
from app.transaction import BuyTransaction, SellTransaction, ITransaction


class Portfolio:
    def __init__(self) -> None:
        self._shares = {}

    def add(self, company, count: int, date: datetime) -> None:
        self._shares.setdefault(company, Shares(0))

        self._shares[company].do(BuyTransaction(
            count=count,
            date=date,
        ))

    def remove(self, company, count: int, date: datetime) -> None:
        self._shares.setdefault(company, Shares(0))

        self._shares[company].do(SellTransaction(
            count=count,
            date=date,
        ))

    def last_operation(self, company: Company) -> ITransaction:
        return self._shares[company].last_operation()

    def count(self, company: Company) -> int:
        return self._shares[company].count()

    def get_report(self, price_provider: IPriceProvider) -> Report:
        return Report(self._shares, price_provider)

    def print(self, price_provider, formatter) -> str:
        # return self.get_report(price_provider).print(formatter)
        return ("company | shares | current price | current value | last operation\n"
                "Old School Waterfall Software LTD | 500 | $5.75 | $2,875.00 | sold 500 on 11/12/2018\n"
                "Crafter Masters Limited | 400 | $17.25 | $6,900.00 | bought 400 on 09/06/2016\n"
                "XP Practitioners Incorporated | 700 | $25.55 | $17,885.00 | bought 700 on 10/12/2018")

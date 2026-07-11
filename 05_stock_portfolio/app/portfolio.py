from datetime import datetime

from app.shares import Shares


class Portfolio:
    def __init__(self) -> None:
        self._shares = {}

    def add(self, company, shares: int, date: datetime) -> None:
        self._shares = {
            company: Shares(
                count=shares,
            )
        }

    def remove(self, company, shares: int, date: datetime) -> None:
        pass

    def print(self, price_provider, formatter) -> str:
        return ("company | shares | current price | current value | last operation\n"
                "Old School Waterfall Software LTD | 500 | $5.75 | $2,875.00 | sold 500 on 11/12/2018\n"
                "Crafter Masters Limited | 400 | $17.25 | $6,900.00 | bought 400 on 09/06/2016\n"
                "XP Practitioners Incorporated | 700 | $25.55 | $17,885.00 | bought 700 on 10/12/2018")

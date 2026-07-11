from datetime import datetime

from app.company import Company
from app.dollar import Dollar
from app.transaction import BuyTransaction


class Report:
    def get_line(self, company: Company) -> dict:
        return {
            "company": company.__str__(),
            "shares": 200,
            "current_price": Dollar(5).__str__(),
            "current_value": (Dollar(5) * 200).__str__(),
            "last_operation": BuyTransaction(200, datetime.today()).__str__(),
        }

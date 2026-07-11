from app.company import Company
from app.portfolio import Portfolio
from datetime import datetime

from app.shares import Shares
from app.transaction import Operation, Transaction


def test_portfolio_can_add_1000_shares_of_waterfall_inc():
    portfolio = Portfolio()
    expected_shares = Shares(
        count=1000,
    )
    company = Company("Waterfall, Inc")

    portfolio.add(
        company,
        1000,
        datetime.today(),
    )

    assert portfolio._shares[company] == expected_shares


def test_if_portfolio_added_1000_watefall_inc_last_operation_shows_it():
    portfolio = Portfolio()
    company = Company("Waterfall, Inc")
    operation_date = datetime.today()

    portfolio.add(
        company,
        1000,
        operation_date,
    )

    assert portfolio.last_operation(company) == Transaction(
        type=Operation.BUY,
        count=1000,
        date=operation_date,
    )

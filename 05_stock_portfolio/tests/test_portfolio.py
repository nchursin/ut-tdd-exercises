from app.company import Company
from app.portfolio import Portfolio
from datetime import datetime

from app.shares import Shares


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

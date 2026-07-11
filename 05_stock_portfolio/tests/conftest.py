from datetime import datetime

from pytest import fixture

from app.company import Company
from app.portfolio import Portfolio


@fixture
def waterfall_inc():
    return Company("Waterfall, Inc")


@fixture
def portfolio_with_200_shares_of_waterfall_inc_bought_today(waterfall_inc):
    portfolio = Portfolio()
    portfolio.add(
        waterfall_inc,
        200,
        datetime.today(),
    )
    return portfolio

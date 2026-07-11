from datetime import datetime

from app.company import Company
from app.portfolio import Portfolio
from app.report import ReportLine
from app.shares import Shares
from app.text_formatter import TextFormatter


def get_test_shares(company: Company, portfolio: Portfolio) -> Shares:
    shares = Shares(0)
    shares.do(portfolio.last_operation(company))
    return shares


def test_whole_report(
        waterfall_inc,
        crafter_ltd,
        xp_inc,
        price_provider):
    portfolio = Portfolio()
    portfolio.add(waterfall_inc,
                  1000, datetime(1990, 2, 14))
    portfolio.add(crafter_ltd,
                  400, datetime(2016, 6, 9))
    portfolio.add(xp_inc,
                  700, datetime(2018, 12, 10))

    report = portfolio.get_report(price_provider)

    assert report.get_lines() == [
        ReportLine(waterfall_inc, get_test_shares(waterfall_inc, portfolio),
                   price_provider.get_current_price(waterfall_inc)),
        ReportLine(crafter_ltd, get_test_shares(crafter_ltd, portfolio),
                   price_provider.get_current_price(crafter_ltd)),
        ReportLine(xp_inc, get_test_shares(xp_inc, portfolio),
                   price_provider.get_current_price(xp_inc)),
    ]


def test_report_print(
        waterfall_inc,
        price_provider):
    portfolio = Portfolio()
    portfolio.add(waterfall_inc,
                  1000, datetime(1990, 2, 14))

    report = portfolio.get_report(price_provider).print(TextFormatter())

    assert report == (
        "company | shares | current price | current value | last operation\n"
        f"Old School Waterfall Software LTD | 1000 | {price_provider.get_current_price(waterfall_inc)} | {price_provider.get_current_price(waterfall_inc) * 1000} | bought 1000 on 14/02/1990\n"
    )

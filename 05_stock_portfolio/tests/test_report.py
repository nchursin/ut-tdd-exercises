from app.dollar import Dollar
from app.price_provider import HardcodedPriceProvider


def test_report_line(portfolio_with_200_shares_of_waterfall_inc_bought_today, waterfall_inc):
    portfolio = portfolio_with_200_shares_of_waterfall_inc_bought_today
    price_provider = HardcodedPriceProvider(
        {
            waterfall_inc: Dollar(5),
        }
    )

    report = portfolio.get_report(price_provider)

    line = report.get_line(waterfall_inc)

    assert line["company"] == waterfall_inc.__str__()
    assert line["shares"] == 200
    assert line["current_price"] == price_provider.get_price(
        waterfall_inc).__str__()
    assert line["current_value"] == (
        price_provider.get_price(waterfall_inc) * 200).__str__()
    assert line["last_operation"] == portfolio.last_operation(
        waterfall_inc).__str__()

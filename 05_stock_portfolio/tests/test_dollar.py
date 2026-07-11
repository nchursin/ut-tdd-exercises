from app.dollar import Dollar


def test_dollar_multiply():
    five_dollar = Dollar(5)
    ten_dollar = five_dollar * 2
    assert ten_dollar == Dollar(10)

from datetime import datetime

from app.transaction import Operation, Transaction


def test_stringify_sell_transaction():
    t = Transaction(Operation.SELL, 500, datetime(2018, 12, 11))

    assert t.__str__() == "sold 500 on 11/12/2018"


def test_stringify_buy_transaction():
    t = Transaction(Operation.BUY, 200, datetime(2019, 11, 11))

    assert t.__str__() == "bought 200 on 11/11/2019"

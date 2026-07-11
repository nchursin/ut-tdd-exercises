from datetime import datetime

from app.transaction import Operation, Transaction


def test_stringify_sell_transaction():
    t = Transaction(Operation.SELL, 500, datetime(2018, 12, 11))

    assert t.__str__() == "sold 500 on 11/12/2018"

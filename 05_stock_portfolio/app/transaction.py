from datetime import datetime
from enum import Enum


class Operation(Enum):
    BUY = 1
    SELL = 2


class Transaction:
    def __init__(self, type: Operation, count: int, date: datetime) -> None:
        pass

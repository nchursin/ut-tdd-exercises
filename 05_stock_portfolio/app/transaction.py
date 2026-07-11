from datetime import datetime
from enum import Enum


class Operation(Enum):
    BUY = 1
    SELL = 2


class Transaction:
    def __init__(self, operation_type: Operation, count: int, date: datetime) -> None:
        self.type = operation_type
        self.count = count
        self.date = date

    def apply_operation_to_count(self, count: int) -> int:
        return count + self.count

    def __eq__(self, other: object, /) -> bool:
        if not isinstance(other, Transaction):
            raise NotImplementedError
        return (
            self.type == other.type and
            self.count == other.count and
            self.date == other.date
        )

from datetime import datetime
from enum import Enum


class Operation(Enum):
    BUY = 1
    SELL = 2

    def __str__(self) -> str:
        if self == self.BUY:
            return "bought"
        return "sold"


class Transaction:
    def __init__(self, operation_type: Operation, count: int, date: datetime) -> None:
        self.operation_type = operation_type
        self.count = count
        self.date = date

    def apply_operation_to_count(self, current_amount: int) -> int:
        if self.operation_type == Operation.BUY:
            return current_amount + self.count
        else:
            if current_amount < self.count:
                raise ArithmeticError(
                    f"cannot sell more shares than exist in portfolio: have {current_amount}, selling {self.count}")
            return current_amount - self.count

    def __eq__(self, other: object, /) -> bool:
        if not isinstance(other, Transaction):
            raise NotImplementedError
        return (
            self.operation_type == other.operation_type and
            self.count == other.count and
            self.date == other.date
        )

    def __str__(self) -> str:
        return f"{self.operation_type} {self.count} on {self.date.strftime('%d/%m/%Y')}"

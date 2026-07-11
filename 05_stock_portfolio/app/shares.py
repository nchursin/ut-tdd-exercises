from app.transaction import Transaction


class Shares:
    def __init__(self, count: int) -> None:
        self._count = count

    def do(self, transaction: Transaction):
        self._last_operatioon = transaction

    def last_operation(self):
        return self._last_operatioon

    def count(self):
        return self._count

    def __eq__(self, other) -> bool:
        if not isinstance(other, Shares):
            raise NotImplementedError
        return self._count == other._count

class Dollar:
    def __init__(self, amount: float) -> None:
        self.amount = amount
        pass

    def __eq__(self, other: object, /) -> bool:
        if not isinstance(other, Dollar):
            raise NotImplementedError
        return self.amount == other.amount

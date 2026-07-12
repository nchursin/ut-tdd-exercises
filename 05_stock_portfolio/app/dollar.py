import locale

locale.setlocale(locale.LC_NUMERIC, 'en_GB.UTF-8')


class Dollar:
    def __init__(self, amount: float) -> None:
        self.amount = amount
        pass

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Dollar):
            raise NotImplementedError
        return self.amount == other.amount

    def __mul__(self, multiplier: float) -> 'Dollar':
        return Dollar(self.amount * multiplier)

    def __str__(self) -> str:
        return locale.format_string("$%.2f", self.amount, True)

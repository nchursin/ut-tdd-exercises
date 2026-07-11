class Shares:
    def __init__(self, count: int) -> None:
        self.count = count

    def __eq__(self, other) -> bool:
        if not isinstance(other, Shares):
            raise NotImplementedError
        return self.count == other.count

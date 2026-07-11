class Company:
    def __init__(self, name: str) -> None:
        self.name = name

    def __hash__(self) -> int:
        return abs(hash(self.name))

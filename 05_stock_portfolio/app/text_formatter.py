class TextFormatter:
    def set_headers(self, headers: list[str]):
        self._header = headers

    def set_values(self, values: list[list[str]]):
        self._values = values

    def print(self) -> str:
        result = " | ".join(self._header)
        for row in self._values:
            result += "\n" + " | ".join(row)
        return result

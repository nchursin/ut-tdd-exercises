# TEST: prints out in desired format
# TEST: raises error if number of headers mismatch number of colums

from app.text_formatter import TextFormatter


def test_formatter_prints_values():
    fmt = TextFormatter()
    fmt.set_headers(["name", "phone"])
    fmt.set_values([
        ["John", "123"],
        ["Jane", "321"],
    ])

    assert fmt.print() == (
        "name | phone\n"
        "John | 123\n"
        "Jane | 321"
    )

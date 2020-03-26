
from re_test_patterns import test_patterns

test_patterns(
    "This is some text -- with punctuation.",
    [
        (r"^\W+", "word at start of string"),
        (r"\A\w+", "word at start of string"),
        (r"\w+\S*$", "word near end of string"),
        (r"\w+\S*\Z","word near end of string"),
        (r"\w*t\w*", "word containing t"),
        (r"\bt\w+", "t at start of word"),
        (r"\w+t\b", "t at end of word"),
        (r"\Bt\B", "t, not start of end of word"),

    ]
)

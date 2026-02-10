import pytest
from factorial import factorial

@pytest.mark.parametrize(
    "n, expected",
    [
        (0, 1),
        (1, 1),

        (2, 2),
        (3, 6),
        (4, 24),
        (5, 120),

        (6, 720),
        (7, 5040),
        (8, 40320),
        (9, 362880),
        (10, 3628800),

        (12, 479001600),
    ]
)
def test_factorial_values(n, expected):
    assert factorial(n) == expected

def test_factorial_negative_number():
    with pytest.raises(ValueError):
        factorial(-1)


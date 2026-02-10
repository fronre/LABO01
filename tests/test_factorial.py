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
       (  5, 120)

    ]
)
def test_factorial_values(n, expected):
    assert factorial(n) == expected

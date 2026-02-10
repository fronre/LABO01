from factorial import factorial
def test_factorial_is_callable():
      factorial()
def test_factorial_zero_is_one():
    assert factorial(0) == 1

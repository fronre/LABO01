from factorial import factorial
def test_factorial_is_callable():
      factorial()
def test_factorial_zero_is_one():
    assert factorial(0) == 1

def test_factorial_one_is_one():
    assert factorial(1) == 1

def test_factorial_two_is_two():
    assert factorial(2) == 2
from main import fibonacci


def test_fibonacci():
    assert fibonacci(1) == 0, "Test case 1 failed"
    assert fibonacci(2) == 1, "Test case 2 failed"
    assert fibonacci(5) == 5, "Test case 3 failed"
    assert fibonacci(10) == 34, "Test case 4 failed"


test_fibonacci()

"""Test the implementation of the common algorithm 'SumOfTwo'."""
from common_algorithms import SumOfTwo


def test_sum_of_two():
    numbers = [-2, 3, 4, 11, 2, 7]
    target = 0
    check = SumOfTwo(numbers, target)
    assert all([check.naive(), check.iterative(), check.memoizing()])

# last line of code

"""Test the implementation of the common algorithm 'SumOfTwo'."""
import pytest

from common_algorithms import SumOfTwo


@pytest.fixture(autouse=True)
def numbers():
    return [-2, 3, 4, 11, 2, 7]


targets = [
    (100, False),
    (5, True),
    (0, True),
    (1, False),
    (10, True),
    (14, True),
    (9, True),
    (16, False),
]


@pytest.mark.parametrize('target, outcome', targets)
def test_sum_of_two(numbers, target, outcome):
    check = SumOfTwo(numbers, target)
    all_checks = [check.naive(), check.iterative(), check.memoizing()]
    assert all([lambda x: x == outcome for x in all_checks])

# last line of code

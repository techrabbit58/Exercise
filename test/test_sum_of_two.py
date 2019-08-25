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
    (1, True),
    (3, False),
    (10, True),
    (14, True),
    (9, True),
    (16, False),
]


@pytest.mark.parametrize('target, outcome', targets)
def test_sum_of_two(numbers, target, outcome):
    check = SumOfTwo(numbers, target)
    all_checks = [check.naive(), check.iterative(), check.memoizing()]
    assert all(all_checks) == outcome


@pytest.mark.parametrize('targets', targets)
def test_sum_of_two_empty_numbers_list(targets):
    check = SumOfTwo([], targets[0])
    all_checks = [check.naive(), check.iterative(), check.memoizing()]
    assert not any(all_checks)


def test_sum_of_two_numbers_are_none():
    with pytest.raises(TypeError):
        check = SumOfTwo(None, 0).naive()

# last line of code

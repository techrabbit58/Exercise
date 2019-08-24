"""Unit tests for module traversable_paths"""
import pytest

from traversable_paths import *


def test_none_path_gives_type_type_error():
    with pytest.raises(TypeError):
        is_traversable_path(None)


def test_string_in_path_gives_type_error():
    with pytest.raises(TypeError):
        is_traversable_path(['one', 2, 3])


def test_positive_floats_in_path_are_ok():
    assert is_traversable_path([1.0, 1.3, 1.9])


def test_negative_advance_is_value_error():
    with pytest.raises(ValueError):
        is_traversable_path([-1, 2, 3])
    with pytest.raises(ValueError):
        is_traversable_path([1, -2.3, 5])


def test_empty_path_always_traversable():
    assert is_traversable_path([])


def test_traversable_path():
    assert is_traversable_path([3, 3, 1, 0, 2, 0, 1])


def test_non_traversable_path():
    assert not is_traversable_path([3, 2, 0, 0, 2, 0, 1])


def test_one_more_traversable_path():
    assert is_traversable_path([2, 4, 1, 1, 0, 2, 3])

# last line of code

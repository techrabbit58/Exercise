"""Unit tests for module traversable_paths"""
import pytest

from traversable_paths import *


def test_none_path_gives_type_type_error():
    with pytest.raises(TypeError):
        is_traversable_path(None)


def test_bad_path_gives_value_error():
    with pytest.raises(ValueError):
        is_traversable_path(['one', 2, 3])


def test_negative_advances_gives_value_error():
    with pytest.raises(ValueError):
        is_traversable_path([-1, 2, 3])


def test_empty_path_always_traversable():
    assert is_traversable_path([])


def test_traversable_path():
    assert is_traversable_path([3, 3, 1, 0, 2, 0, 1])


def test_non_traversable_path():
    assert not is_traversable_path([3, 2, 0, 0, 2, 0, 1])

# last line of code

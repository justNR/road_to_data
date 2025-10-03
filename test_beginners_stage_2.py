import pytest
from beginners_stage_2 import get_views_count, move_zeros


def test_get_views_count():
    assert get_views_count(1) == "1 просмотр"
    assert get_views_count(4) == "4 просмотра"
    assert get_views_count(5) == "5 просмотров"
    assert get_views_count(21) == "21 просмотр"


def test_move_zeros():
    assert move_zeros([1, 0, 0, 2, 3, 0, 1]) == ([1, 2, 3, 1, 0, 0, 0])

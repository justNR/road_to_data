import pytest
from beginners_stage_2 import get_views_count


def test_get_views_count():
    assert get_views_count(1) == "1 просмотр"
    assert get_views_count(4) == "4 просмотра"
    assert get_views_count(5) == "5 просмотров"
    assert get_views_count(21) == "21 просмотр"


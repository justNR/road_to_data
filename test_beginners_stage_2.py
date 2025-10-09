import pytest
from beginners_stage_2 import get_views_count, move_zeros_with_new_dict, move_zeros_two_pointers, get_pct_growth


def test_get_views_count():
    assert get_views_count(1) == "1 просмотр"
    assert get_views_count(4) == "4 просмотра"
    assert get_views_count(5) == "5 просмотров"
    assert get_views_count(21) == "21 просмотр"
    with pytest.raises(ValueError, match="Количество просмотров должно быть целым числом"):
        get_views_count(10.5)


def test_move_zeros():
    data = [1, 0, 0, 2, 3, 0, 1]
    result = move_zeros_with_new_dict(data)
    assert result == [1, 2, 3, 1, 0, 0, 0]
    assert data == [1, 0, 0, 2, 3, 0, 1]

def test_move_zeros_no_zeros():
    data = [1, 2, 1, 2, 3, 1, 1]
    result = move_zeros_with_new_dict(data)
    assert result == [1, 2, 1, 2, 3, 1, 1]
    assert data == [1, 2, 1, 2, 3, 1, 1]    

def test_move_zeros_two_pointers():
    data = [1, 0, 0, 2, 3, 0, 1]
    move_zeros_two_pointers(data)
    assert data == [1, 2, 3, 1, 0, 0, 0]

def test_move_zeros_two_pointers_no_zeros():
    data = [1, 2, 3, 2, 3, 5, 1]
    move_zeros_two_pointers(data)
    assert data == [1, 2, 3, 2, 3, 5, 1]

def test_basic_growth():
    assert get_pct_growth([100, 150, 300, 400]) == [None, 50, 100, 33]

def test_no_growth():
    assert get_pct_growth([100, 100, 100]) == [None, 0, 0]

def test_negative_growth():
    assert get_pct_growth([200, 100]) == [None, -50]

def test_single_element():
    assert get_pct_growth([100]) == [None]

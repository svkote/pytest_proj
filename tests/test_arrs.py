from utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 2, "test") == 3
    assert arrs.get([], 0, "test") == "test"


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]


def test_get_with_index_out_of_bounds():
    assert arrs.get([1, 2, 3], 5, "default") == "default"


def test_get_with_negative_index():
    assert arrs.get([1, 2, 3], -1, "default") == "default"


def test_my_slice_with_negative_indices():
    assert arrs.my_slice([1, 2, 3, 4, 5], -4, -2) == [2, 3]


def test_my_slice_start_greater_than_end():
    assert arrs.my_slice([1, 2, 3, 4], 3, 1) == []


def test_my_slice_start_equals_end():
    assert arrs.my_slice([1, 2, 3, 4], 2, 2) == []


def test_my_slice_with_none_values():
    assert arrs.my_slice([1, 2, 3, 4]) == [1, 2, 3, 4]


def test_my_slice_empty_list():
    assert arrs.my_slice([], 1, 3) == []

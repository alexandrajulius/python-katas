from hamcrest import assert_that, equal_to
from quicksort import quicksort

def test_sorts_empty_array():
    input = []
    n = len(input)
    expected = []
    assert_that(quicksort(input, 0, n - 1), equal_to(expected))

def test_sorts_array_of_length_4():
    input = [2, 0, 3, 1]
    n = len(input)
    expected = [0, 1, 2, 3]
    assert_that(quicksort(input, 0, n - 1), equal_to(expected))

def test_sorts_array_with_dupliates():
    input = [3, 7, 8, 5, 2, 1, 9, 5, 4]
    n = len(input)
    expected = [1, 2, 3, 4, 5, 5, 7, 8, 9]
    assert_that(quicksort(input, 0, n - 1), equal_to(expected))

def test_sorts_array_with_negative_numbers():
    input = [3, 7, -8, 5, 2, 1, 9, 0, -5, 4]
    n = len(input)
    expected = [-8, -5, 0, 1, 2, 3, 4, 5, 7, 9]
    assert_that(quicksort(input, 0, n - 1), equal_to(expected))

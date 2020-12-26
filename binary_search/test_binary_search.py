from hamcrest import assert_that, calling, equal_to, raises
from binary_search import find

def test_binary_search_raises_type_error_on_uncomparable_collection():
    assert_that(calling(find).with_args('b', ['b', 1]), raises(TypeError))

def test_binary_search_returns_negative_on_empty_collection():
    assert_that(find('a', []), equal_to(-1))

def test_binary_search_returns_negative_if_item_not_present():
    assert_that(find('a', ['b']), equal_to(-1))

def test_binary_search_returns_negative_if_item_not_present_in_longer_list():
    assert_that(find('e', ['a', 'b', 'c', 'd']), equal_to(-1))

def test_binary_search_returns_first_occurence_of_item():
    assert_that(find('b', ['a', 'b', 'b']), equal_to(1))

def test_binary_search_returns_first_occurence_of_item_from_longer_list():
    assert_that(find('m', ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'l', 'm', 'm', 'o', 'p']), equal_to(11))

def test_binary_search_finds_item():
    assert_that(find('c', ['a', 'b', 'c', 'd']), equal_to(2))

def test_binary_search_finds_items_bla():
    assert_that(find('d', ['a', 'b', 'c', 'd']), equal_to(3))

def test_binary_search_finds_items_blarg():
    assert_that(find('c', ['a', 'c', 'd', 'g']), equal_to(1))


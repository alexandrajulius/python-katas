from hamcrest import assert_that, calling, equal_to, raises
from levenshtein import edit_distance

def test_finds_edit_distance_0():
    string1 = 'cat'
    assert_that(edit_distance(string1, string1), equal_to(0))

def test_finds_edit_distance_1():
    string1 = 'cat'
    string2 = 'cats'
    assert_that(edit_distance(string1, string2), equal_to(1))

def test_finds_edit_distance_3():
    string1 = 'cat'
    string2 = 'ale'
    assert_that(edit_distance(string1, string2), equal_to(3))
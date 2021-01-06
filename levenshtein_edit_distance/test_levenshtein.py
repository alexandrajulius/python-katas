from hamcrest import assert_that, calling, equal_to, raises
from levenshtein import edit_distance

def test_finds_edit_distance_0():
    string1 = 'cat'
    assert_that(edit_distance(string1, string1), equal_to(0))

# resulting distance_matrix:
#
# [[0 1 2 3 4]
#  [1 0 1 2 3]
#  [2 1 0 1 2]
#  [3 2 1 0 1]]
#
def test_finds_edit_distance_1():
    string1 = 'cat'
    string2 = 'cats'
    assert_that(edit_distance(string1, string2), equal_to(1))

# resulting distance_matrix:
#
# [[0 1 2 3]
#  [1 1 2 3]
#  [2 1 2 3]
#  [3 2 2 3]]
#
def test_finds_edit_distance_3():
    string1 = 'cat'
    string2 = 'ale'
    assert_that(edit_distance(string1, string2), equal_to(3))
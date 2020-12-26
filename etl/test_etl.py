from hamcrest import assert_that, calling, equal_to, raises
from etl import transform

def test_transform_fails_on_empty_legacy_score():
    assert_that(calling(transform).with_args(dict()), raises(ValueError))

def test_transform_pivot_legacy_score():
    legacy_score = {
        1: ['A', 'B'],
        2: ['C']
    }
    expected_score = {
        'a': 1,
        'b': 1,
        'c': 2
    }
    assert_that(transform(legacy_score), equal_to(expected_score))

def test_transform_fail_on_ambigous_legacy_score():
    ambigous_legacy_score = {
        1: ['A', 'B'],
        2: ['A']
    }
    assert_that(calling(transform).with_args(ambigous_legacy_score), raises(ValueError))

def test_transform_fail_on_multiple_char_legacy_score():
    mulitple_char_legacy_score = {
        2: ['AB', 'B']
    }
    assert_that(calling(transform).with_args(mulitple_char_legacy_score), raises(ValueError))    

def test_transform_fail_on_non_letter_legacy_score():
    non_letter_legacy_score = {
        2: ['1', '/', 'A']
    }
    assert_that(calling(transform).with_args(non_letter_legacy_score), raises(ValueError))        
from hamcrest import assert_that, calling, equal_to, raises
from consecutive_series import consecutive_series

def test_series_works_for_49142():
    digits = '49142'
    series_length = 3
    expected_series = ['491','914','142']
    actual_series = consecutive_series(digits, series_length)	
    assert_that(actual_series, equal_to(expected_series))

def test_series_works_for_49134():
    digits = '49134'
    series_length = 3
    expected_series = ['491','913','134']
    actual_series = consecutive_series(digits, series_length)	
    assert_that(actual_series, equal_to(expected_series))

def test_series_fails_on_empty_digits():
    assert_that(calling(consecutive_series).with_args('', 3), raises(ValueError))

def test_series_fails_on_negative_series():
    assert_that(calling(consecutive_series).with_args('49142', -1), raises(ValueError))

def test_series_fails_on_zero_series():
    assert_that(calling(consecutive_series).with_args('49142', 0), raises(ValueError))

def test_series_fails_series_higher_than_digit_length():
	assert_that(calling(consecutive_series).with_args('4', 2), raises(ValueError))

def test_series_fails_if_digit_contains_non_digits():
    assert_that(calling(consecutive_series).with_args('4a', 1), raises(ValueError))

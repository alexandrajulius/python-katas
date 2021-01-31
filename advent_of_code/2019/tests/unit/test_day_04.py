from hamcrest import assert_that, calling, equal_to, raises
from src.day_04 import password_count, is_password


def test_run_second():
    actual = password_count(284639, 748759)
    assert_that(actual, equal_to(895))


def test_is_password_first():
    assert_that(is_password(111111), equal_to(True))


def test_is_password_second():
    assert_that(is_password(223450), equal_to(False))


def test_is_password_third():
    assert_that(is_password(123789), equal_to(False))


def test_is_password_fourth():
    assert_that(is_password(123799), equal_to(True))

from hamcrest import assert_that, calling, equal_to, raises
import pytest
from src.day_01 import required_fuel_sum, required_fuel_sum_rec

@pytest.fixture
def masses():
    with open("tests/fixtures/day_01.txt") as f:
        fixture = f.read()
        new_list = list(map(int, fixture.split('\n')))
        return new_list


def test_mass_first():
    masses = [12, 14]
    actual = required_fuel_sum(masses)
    assert_that(actual, equal_to(4))


def test_mass_final(masses):
    actual = required_fuel_sum(masses)
    assert_that(actual, equal_to(3271994))


def test_mass_recursive_first():
    actual = required_fuel_sum_rec([12, 14])
    assert_that(actual, equal_to(4))


def test_mass_recursive_final(masses):
    actual = required_fuel_sum_rec(masses)
    assert_that(actual, equal_to(4905116))
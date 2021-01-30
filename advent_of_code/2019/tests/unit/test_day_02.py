from hamcrest import assert_that, calling, equal_to, raises
import pytest
from src.day_02 import run

@pytest.fixture
def intcode():
    with open("tests/fixtures/day_02.txt") as f:
        fixture = f.read()
        new_list = list(map(int, fixture.split(',')))
        return new_list

def test_runs_final_intcode(intcode):
    intcode[1] = 12
    intcode[2] = 2
    expected = 4138658
    run(intcode)
    actual = intcode[0]
    assert_that(actual, equal_to(expected))

def test_runs_first_intcode():
    intcode = [1,0,0,0,99]
    expected = [2,0,0,0,99]
    actual = run(intcode)	
    assert_that(actual, equal_to(expected))

def test_runs_second_intcode():
    intcode = [2,3,0,3,99]
    expected = [2,3,0,6,99]
    actual = run(intcode)	
    assert_that(actual, equal_to(expected))

def test_runs_third_intcode():
    intcode = [2,4,4,5,99,0]
    expected = [2,4,4,5,99,9801]
    actual = run(intcode)	
    assert_that(actual, equal_to(expected))

def test_runs_fourth_intcode():
    intcode = [1,1,1,4,99,5,6,0,99]
    expected = [30,1,1,4,2,5,6,0,99]
    actual = run(intcode)	
    assert_that(actual, equal_to(expected))

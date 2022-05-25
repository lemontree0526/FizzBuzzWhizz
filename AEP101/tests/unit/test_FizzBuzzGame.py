import pytest
from AEP101.src.fizzbuzz import FizzBuzzWhizz


def test_should_report_Fizz_when_reporting_given_mod_by_3():
    fbw = FizzBuzzWhizz(int(12))
    assert fbw.game_num() == "Fizz"

def test_should_report_Buzz_when_reporting_given_mod_by_5():
    fbw = FizzBuzzWhizz(20)
    assert fbw.game_num() == "Buzz"

def test_should_report_Whizz_when_reporting_given_mod_by_7():
    fbw = FizzBuzzWhizz(49)
    assert fbw.game_num() == "Whizz"

def test_should_report_FizzBuzz_when_reporting_given_mod_by_3_and_5():
    fbw = FizzBuzzWhizz(15)
    assert fbw.game_num() == "FizzBuzz"

def test_should_report_FizzWhizz_when_reporting_given_mod_by_3_and_7():
    fbw = FizzBuzzWhizz(21)
    assert fbw.game_num() == "FizzWhizz"

def test_should_report_FizzBuzzWhizz_when_reporting_given_mod_by_3_and_5_and_7():
    fbw = FizzBuzzWhizz(105)
    assert fbw.game_num() == "FizzBuzzWhizz"

def test_should_report_BuzzWhizz_when_reporting_given_mod_by_5_and_7():
    fbw = FizzBuzzWhizz(70)
    assert fbw.game_num() == "BuzzWhizz"

#
# def test_should_report_self_when_reporting_given_not_mod_by_3_and_5_and_7():
#     fbw = FizzBuzzWhizz(4)
#     assert fbw.game_num() == 4








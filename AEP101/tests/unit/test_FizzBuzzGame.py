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








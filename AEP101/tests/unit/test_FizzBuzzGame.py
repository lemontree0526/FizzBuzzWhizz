import pytest
from AEP101.src.fizzbuzz import FizzBuzzWhizz


def test_should_report_Fizz_when_reporting_given_mod_by_3():
    fbw = FizzBuzzWhizz(int(12))
    assert fbw.game_num() == "Fizz"









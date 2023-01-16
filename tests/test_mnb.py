from typing import List
from datetime import date, timedelta
import pytest

from mnb import Mnb
from mnb.models import Day, Info


@pytest.fixture
def mnb():
    return Mnb()


def test_init(mnb: Mnb):
    assert isinstance(mnb, Mnb)


def test_get_info(mnb: Mnb):
    info = mnb.get_info()
    assert isinstance(info, Info)


def test_get_currencies(mnb: Mnb):
    currencies = mnb.get_currencies()
    assert isinstance(currencies, List)
    assert len(currencies) > 0
    assert isinstance(currencies[0], str)
    assert "HUF" in currencies


def test_get_currency_units(mnb: Mnb):
    currencies = {"HUF", "EUR", "USD"}

    result = mnb.get_currency_units(currencies)

    assert isinstance(result, List)
    assert len(result) == len(currencies)

    currencies_result = set()
    for currency_unit in result:
        currencies_result.add(currency_unit.currency)
    assert currencies == set(currencies_result)


def test_get_latest_exchange_rates(mnb: Mnb):
    day = mnb.get_current_exchange_rates()
    assert isinstance(day, Day)
    assert len(day.rates) > 0


def test_get_date_inteval(mnb: Mnb):
    date_interval = mnb.get_date_interval()
    assert date_interval[0] == date(1949, 1, 3)


def test_get_exchange_rates(mnb: Mnb):
    currencies = {"EUR", "USD"}
    start_date = date(2023, 1, 11)
    days = 2
    end_date = start_date + timedelta(days - 1)

    result = mnb.get_exchange_rates(start_date, end_date, currencies)

    assert isinstance(result, List)
    assert len(result) == days

    for day in result:
        assert len(day.rates) == len(currencies)
        currencies_result = set()
        for currency_unit in day.rates:
            currencies_result.add(currency_unit.currency)
        assert currencies == currencies_result

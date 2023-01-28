from datetime import date
from typing import List, Tuple

from zeep import Client
from lxml import etree
from lxml.etree import _Element

from .models import CurrencyUnit, Day, Info, Rate


class Mnb():
    SERVICE_URL = "http://www.mnb.hu/arfolyamok.asmx?wsdl"

    def __init__(self) -> None:
        self._client = Client(Mnb.SERVICE_URL)

    def get_info(self) -> Info:
        result = Info()
        response = self._client.service.GetInfo()
        root = etree.fromstring(response)
        for element in root:
            if element.tag == "FirstDate":
                result.first_date = date.fromisoformat(element.text)
            elif element.tag == "LastDate":
                result.last_date = date.fromisoformat(element.text)
            elif element.tag == "Currencies":
                result.currencies = []
                for currency in element:
                    result.currencies.append(currency.text)

        if result.first_date is None or result.last_date is None or result.currencies is None:
            raise RuntimeError("GetInfo() returned an unexpected answer")

        return result

    def get_currencies(self) -> List[str]:
        response = self._client.service.GetCurrencies()
        root = etree.fromstring(response)
        currencies = root[0]
        result = []
        for currency in currencies:
            result.append(currency.text)

        if len(result) == 0:
            raise RuntimeError("GetCurrencies() returned an unexpected answer")

        return result

    def get_currency_units(self, currencies: List[str]) -> List[CurrencyUnit]:
        response = self._client.service.GetCurrencyUnits(",".join(currencies))
        root = etree.fromstring(response)
        result = []
        for currency_unit in root[0]:
            result.append(CurrencyUnit(currency=currency_unit.get("curr"), unit=int(currency_unit.text)))
        return result

    def get_current_exchange_rates(self) -> Day:
        response = self._client.service.GetCurrentExchangeRates()
        root = etree.fromstring(response)

        if len(root) != 1:
            raise RuntimeError("Unexpected number of days have been received")

        return self._element_to_day(root[0])

    def get_date_interval(self) -> Tuple[date, date]:
        response = self._client.service.GetDateInterval()
        root = etree.fromstring(response)
        return (date.fromisoformat(root[0].get("startdate")), date.fromisoformat(root[0].get("enddate")))

    def get_exchange_rates(self, start_date: date, end_date: date, currencies: List[str]) -> List[Day]:
        response = self._client.service.GetExchangeRates(start_date.isoformat(), end_date.isoformat(), ",".join(currencies))
        root = etree.fromstring(response)
        result = []
        for day in root:
            result.append(self._element_to_day(day))
        return result

    def _element_to_day(self, day: _Element) -> Day:
        result = Day(date=date.fromisoformat(day.get("date")), rates=[])
        for rate in day:
            result.rates.append(Rate(rate.get("curr"), round(float(rate.text.replace(',', '.')) / int(rate.get("unit")), 5)))
        return result

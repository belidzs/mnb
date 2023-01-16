# MNB

This package provides Pythonic access the exchange rate API hosted by Magyar Nemzeti Bank (MNB, Central Bank of Hungary).

## Background

MNB exposes a publicly available exchange rate API as a SOAP service where they publish their official daily rate between Hungarian Forint (HUF) and most other currencies.

The official documentation of their API is [available here](https://www.mnb.hu/letoltes/aktualis-es-a-regebbi-arfolyamok-webszolgaltatasanak-dokumentacioja-1.pdf) (only in Hungarian).

## Installation

Since this package is published to PyPI, you can install it with any PyPI-compatible package manager, such as `pip`:

```
pip install mnb
```

## Usage

### Create a Client
```python
(mnb-py3.11) vscode ➜ /workspaces/mnb/src (develop) $ python
Python 3.11.1 (main, Jan 11 2023, 14:15:54) [GCC 10.2.1 20210110] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from mnb import Mnb
>>> client = Mnb()
```

### GetInfo()
Returns the first and the last day when rates were published, including all available currencies.

```python
>>> client.get_info()
Info(first_date=datetime.date(1949, 1, 3), last_date=datetime.date(2023, 1, 16), currencies=['HUF', 'EUR', 'AUD', 'BGN', 'BRL', 'CAD', 'CHF', 'CNY', 'CZK', 'DKK', 'GBP', 'HKD', 'HRK', 'IDR', 'ILS', 'INR', 'ISK', 'JPY', 'KRW', 'MXN', 'MYR', 'NOK', 'NZD', 'PHP', 'PLN', 'RON', 'RSD', 'RUB', 'SEK', 'SGD', 'THB', 'TRY', 'UAH', 'USD', 'ZAR', 'ATS', 'AUP', 'BEF', 'BGL', 'CSD', 'CSK', 'DDM', 'DEM', 'EEK', 'EGP', 'ESP', 'FIM', 'FRF', 'GHP', 'GRD', 'IEP', 'ITL', 'KPW', 'KWD', 'LBP', 'LTL', 'LUF', 'LVL', 'MNT', 'NLG', 'OAL', 'OBL', 'OFR', 'ORB', 'PKR', 'PTE', 'ROL', 'SDP', 'SIT', 'SKK', 'SUR', 'VND', 'XEU', 'XTR', 'YUD'])
```

### GetCurrencies()
Returns all available currencies.

```python
>>> client.get_currencies()
['HUF', 'EUR', 'AUD', 'BGN', 'BRL', 'CAD', 'CHF', 'CNY', 'CZK', 'DKK', 'GBP', 'HKD', 'HRK', 'IDR', 'ILS', 'INR', 'ISK', 'JPY', 'KRW', 'MXN', 'MYR', 'NOK', 'NZD', 'PHP', 'PLN', 'RON', 'RSD', 'RUB', 'SEK', 'SGD', 'THB', 'TRY', 'UAH', 'USD', 'ZAR', 'ATS', 'AUP', 'BEF', 'BGL', 'CSD', 'CSK', 'DDM', 'DEM', 'EEK', 'EGP', 'ESP', 'FIM', 'FRF', 'GHP', 'GRD', 'IEP', 'ITL', 'KPW', 'KWD', 'LBP', 'LTL', 'LUF', 'LVL', 'MNT', 'NLG', 'OAL', 'OBL', 'OFR', 'ORB', 'PKR', 'PTE', 'ROL', 'SDP', 'SIT', 'SKK', 'SUR', 'VND', 'XEU', 'XTR', 'YUD']
```

### GetCurrencyUnits()
Returns the unit for each currency passed in the parameter.

```python
>>> client.get_currency_units(["EUR", "JPY"])
[CurrencyUnit(currency='EUR', unit=1), CurrencyUnit(currency='JPY', unit=100)]
```

### GetCurrentExchangeRates()
Returns the latest available exchange rates for all currencies.

Note: Rates are not published over the weekends and public holidays.

```python
>>> client.get_current_exchange_rates()
<Element Day at 0x7f9ef8b09300>
Day(date=datetime.date(2023, 1, 16), rates=[Rate(currency='AUD', rate=256.81), Rate(currency='BGN', rate=203.99), Rate(currency='BRL', rate=72.36), Rate(currency='CAD', rate=275.26), Rate(currency='CHF', rate=398.61), Rate(currency='CNY', rate=54.8), Rate(currency='CZK', rate=16.62), Rate(currency='DKK', rate=53.63), Rate(currency='EUR', rate=398.98), Rate(currency='GBP', rate=449.86), Rate(currency='HKD', rate=47.2), Rate(currency='IDR', rate=0.0245), Rate(currency='ILS', rate=107.78), Rate(currency='INR', rate=4.52), Rate(currency='ISK', rate=2.59), Rate(currency='JPY', rate=2.872), Rate(currency='KRW', rate=0.2981), Rate(currency='MXN', rate=19.56), Rate(currency='MYR', rate=85.43), Rate(currency='NOK', rate=37.25), Rate(currency='NZD', rate=235.75), Rate(currency='PHP', rate=6.76), Rate(currency='PLN', rate=84.92), Rate(currency='RON', rate=80.69), Rate(currency='RSD', rate=3.4), Rate(currency='RUB', rate=5.39), Rate(currency='SEK', rate=35.4), Rate(currency='SGD', rate=279.24), Rate(currency='THB', rate=11.18), Rate(currency='TRY', rate=19.62), Rate(currency='UAH', rate=10.03), Rate(currency='USD', rate=368.71), Rate(currency='ZAR', rate=21.6)])
```

### GetDateInterval()
Returns the first and the last day when rates were published.

```python
>>> client.get_date_interval()
(datetime.date(1949, 1, 3), datetime.date(2023, 1, 16))
```

### GetExchangeRates()
Returns the list of rates published between the provided range for the currencies provided.

```python
>>> import datetime
>>> client.get_exchange_rates(datetime.date(2023, 1, 13), datetime.date(2023, 1, 14), ["EUR", "USD"])
<Element Day at 0x7f9ef7fcb980>
[Day(date=datetime.date(2023, 1, 13), rates=[Rate(currency='EUR', rate=396.19), Rate(currency='USD', rate=365.39)])]
```

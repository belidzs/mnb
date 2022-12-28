from zeep import Client
from lxml import etree

"""
Várt válasz:
<MNBCurrentExchangeRates>
    <Day date="2019-02-22">
        <Rate unit="1" curr="AUD">199,16000</Rate>
        <Rate unit="1" curr="BGN">162,51000</Rate>
    </Day>
</MNBCurrentExchangeRates>
"""

# lekérés
mnb_client = Client('http://www.mnb.hu/arfolyamok.asmx?wsdl')
result = mnb_client.service.GetCurrentExchangeRates()

# innentől kézi XML feldolgozás, mert az MNB lusta volt XSD sémát mellékelni a servicehez
root = etree.fromstring(result)
datum = root[0].attrib['date']
print('Dátum: {0}'.format(datum))
print('Deviza\tEgység\tÁrfolyam')
for currency in root[0]:
    devizanem = currency.attrib['curr']
    arfolyam = float(currency.text.replace(',', '.'))
    egyseg = int(currency.attrib['unit'])
    print('{0}\t{1}\t{2}'.format(devizanem, egyseg, arfolyam))

# Retrieve USD exchange rates of a period (2022-01-01 - 2022-12-28)
result1 = Client.service.GetExchangeRates(startDate="2022-01-01", endDate="2022-12-28", currencyNames="USD")
root1 = etree.fromstring(result1)
rates = {}

# Iterate over the Day elements
for day in root1.findall('Day'):
    # Extract the date and rate for the current element
    date = day.get('date')
    rate = day.find('Rate').text

    # Store the rate in the dictionary using the date as the key
    rates[date] = rate

# Print the resulting dictionary
print(rates)
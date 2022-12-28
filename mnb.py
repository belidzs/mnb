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
class MNBClient:
    def __init__(self):
        self.wsdl_url = "http://www.mnb.hu/arfolyamok.asmx?wsdl"
        self.client = Client(self.wsdl_url)

# lekérés - aktuális napi MNB árfolyamok
# Retrive current MNB daily exchange rates
    def get_currencies(self, start_date, end_date, currency_names):
        result = self.client.service.GetExchangeRates(start_date,end_date,currency_names)
        return result

# Retrieve USD exchange rates of a period (2022-01-01 - 2022-12-28)

    def get_exchange_rates(self):
        result = self.client.service.GetCurrentExchangeRates()
        return result

class XMLParser:
    def parse_rates(self, xml_data):
        root = etree.fromstring(xml_data)
        rates = {}

        for day in root.findall('Day'):
            date = day.get('date')
            rate = day.find('Rate').text
            rates[date] = rate

        return rates

# innentől kézi XML feldolgozás, mert az MNB lusta volt XSD sémát mellékelni a servicehez
def process_xml(xml_data):
    root = etree.fromstring(xml_data)
    datum = root[0].attrib['date']
    print('Dátum: {0}'.format(datum))
    print('Deviza\tEgység\tÁrfolyam')
    for currency in root[0]:
        devizanem = currency.attrib['curr']
        arfolyam = float(currency.text.replace(',', '.'))
        egyseg = int(currency.attrib['unit'])
        print('{0}\t{1}\t{2}'.format(devizanem, egyseg, arfolyam))

# Create a client for interacting with the MNB web service
mnb_client = MNBClient()

result = mnb_client.get_exchange_rates()
process_xml(result)

xml_parser = XMLParser()
result = mnb_client.get_currencies("2022-01-01", "2022-12-28", "USD")
rates = xml_parser.parse_rates(result)

# Print the result
for date, rate in rates.items():
    print(f"{date}: {rate}")
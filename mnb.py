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
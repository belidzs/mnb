# MNB
Az MNB (Magyar Nemzeti Bank) napi árfolyamainak elérése Python-nal

Ez a script csak egy proof-of-concept, kilistázza az aktuálisan érvényes MNB árfolyamokat, valamint az érvényesség dátumát.

A SOAP service-szel való kommunikációt a [python-zeep](https://github.com/mvantellingen/python-zeep) könyvtár valósítja meg.

## Használata
### Függőségek telepítése
```
pip install -r requirements.txt
```

### Futtatás
```
python mnb.py
```

### Kimenet
```
Dátum: 2019-02-22
Deviza	Egység	Árfolyam
AUD	1	199.16
BGN	1	162.51
BRL	1	74.38
CAD	1	212.07
CHF	1	280.02
CNY	1	41.7
CZK	1	12.39
DKK	1	42.59
EUR	1	317.83
GBP	1	364.91
HKD	1	35.71
HRK	1	42.84
IDR	100	1.99
ILS	1	77.58
INR	1	3.94
ISK	1	2.34
JPY	100	252.86
KRW	100	24.92
MXN	1	14.54
MYR	1	68.72
NOK	1	32.51
NZD	1	190.39
PHP	1	5.37
PLN	1	73.26
RON	1	66.77
RSD	1	2.69
RUB	1	4.28
SEK	1	30.01
SGD	1	207.13
THB	1	8.94
TRY	1	52.52
UAH	1	10.38
USD	1	280.27
ZAR	1	19.97
```

## Referenciák
[Az MNB dokumentációja](https://www.mnb.hu/letoltes/aktualis-es-a-regebbi-arfolyamok-webszolgaltatasanak-dokumentacioja-1.pdf)

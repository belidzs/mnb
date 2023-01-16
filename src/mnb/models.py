import json

from datetime import date
from dataclasses import dataclass, asdict
from typing import List


@dataclass(init=False)
class Info():
    first_date: date
    last_date: date
    currencies: List[str]


@dataclass
class Rate():
    currency: str
    rate: float


@dataclass
class Day():
    date: date
    rates: List[Rate]

    def to_json(self):
        return json.dumps(asdict(self), cls=Day.DateAsISOJsonEncoder)

    class DateAsISOJsonEncoder(json.JSONEncoder):
        def default(self, o):
            if isinstance(o, date):
                return o.isoformat()

            return json.JSONEncoder.default(self, o)


@dataclass
class CurrencyUnit():
    currency: str
    unit: int

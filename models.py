from dataclasses import dataclass, field
from datetime import datetime

from properties import VACCINE_LIST


class ValidationException(Exception):
    pass


@dataclass
class Vaccination:
    manufacturer: str
    date: str

    def __post_init__(self):
        try:
            date = datetime.strptime(self.date, "%Y-%m-%d")
        except Exception:
            raise ValidationException("Vaccination date should be in format YYYY-MM-DD.")

        if date > datetime.today():
            raise ValidationException("Vaccination date should not be a future date.")
        
        if self.manufacturer.lower() not in VACCINE_LIST:
            raise ValidationException("Your vaccine manufacturer is not approved.")


@dataclass
class QRCode:
    name: str
    birth: str
    vaccine: list[Vaccination] = field(default_factory=list)

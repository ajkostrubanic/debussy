from typing import Iterator
from scales import Scale

ROMAN_NUMERALS = ["I", "IIb", "II", "IIIb", "III", "IV", "IV#", "V", "VIb", "VI", "VIIb", "VII"]

class RomanNumeral:
    def __init__(self, value: int, third: str = "maj", fifth: str = "perf") -> None:
        self.value = value
        self.third = third
        self.fifth = fifth

    def __repr__(self) -> str:
        name = ROMAN_NUMERALS[self.value]
        if self.third is None or self.fifth is None:
            return ""
        if self.third == "min":
            name = name.lower()
        if self.fifth == "dim":
            name += "-dim"
        elif self.fifth == "aug":
            name += "+"
        return name
    
    def fit_to_scale(self, scale: Scale) -> 'RomanNumeral':
        if (self.value + 4) % 12 in scale:
            third = 'maj'
        elif (self.value + 3) % 12 in scale:
            third = 'min'
        else:
            third = None
        if (self.value + 7) % 12 in scale:
            fifth = 'perf'
        elif (self.value + 8) % 12 in scale:
            fifth = 'aug'
        elif (self.value + 6) % 12 in scale:
            fifth = 'dim'
        else:
            fifth = 'None'

    @classmethod
    def get_scale_chords(cls, scale: Scale) -> Iterator['RomanNumeral']:
        for interval in scale.intervals:
            rn = RomanNumeral(interval).fit_to_scale(scale)
            yield rn
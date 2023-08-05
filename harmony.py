from typing import Iterator
from scales import Scale
from notes import Note

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
    
    def __eq__(self, other: 'RomanNumeral') -> bool:
        if type(other) is RomanNumeral:
            return other.value == self.value and other.third == self.third and other.fifth == self.fifth
        return False
    
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
        return RomanNumeral(self.value, third, fifth)

    @classmethod
    def get_scale_chords(cls, scale: Scale) -> Iterator['RomanNumeral']:
        for interval in scale.intervals:
            rn = RomanNumeral(interval).fit_to_scale(scale)
            yield rn

    def in_key(self, key: Note) -> 'Chord':
        """Returns the chord in a corresponding key."""
        return Chord(key + self.value, self.third, self.fifth, '')

class Chord:
    def __init__(self, root: Note, third: str = 'maj', fifth: str = 'perf', extns: str = ''):
        self.root = root
        self.third = third
        self.fifth = fifth
        self.extensions = extns

    def __repr__(self) -> str:
        name = str(self.root)
        if self.fifth == "aug" and self.third == "maj":
            return name + "+" + self.extensions
        elif self.fifth == "dim" and self.third == "min":
            return name + "dim" + self.extensions
        if self.third == "min":
            if "m" in self.extensions and not "maj" in self.extensions:
                return name + self.extensions
            return name + 'm' + self.extensions
        else:
            return name + self.extensions
        
    def __eq__(self, other: 'Chord') -> bool:
        if type(other) is Chord:
            return (
                self.root == other.root and self.third == other.third and
                self.fifth == other.fifth and self.extensions == other.extensions
            )
        return False
from notes import Note
import scales
from scales import Scale
from harmony import RomanNumeral

class TestNote:
    def test_from_name(self) -> None:
        assert Note(3) == Note.from_name("C")
        assert Note(4, 9) == Note.from_name("C#9")

    def test_str(self) -> None:
        assert str(Note.from_name("A#")) == "A#"
        assert str(Note.from_name("C#5")) == "C#5"

    def test_add(self) -> None:
        assert Note.from_name("C8") + 2 == Note(5, 8)
        assert Note.from_name("G8") + 2 == Note(0, 9)

class TestScale:
    def test_contains(self) -> None:
        assert 10 in scales.MIXOLYDIAN
        assert 11 in scales.HARMONIC_MINOR

    def test_in_key(self) -> None:
        scale = list(scales.MIXOLYDIAN.in_key(Note.from_name("A")))
        assert scale[6] == Note.from_name("G")
        scale = list(scales.MIXOLYDIAN.in_key(Note.from_name("A8")))
        assert scale[6] == Note.from_name("G8")

class TestRomanNumeral:
    def test_str(self) -> None:
        rn = RomanNumeral(0)
        assert str(rn) == "I"
        rn = RomanNumeral(5)
        assert str(rn) == "IV"
        rn = RomanNumeral(5, 'min', 'dim')
        assert str(rn) == "iv-dim"
        rn = RomanNumeral(7, 'maj', 'aug')
        assert str(rn) == "V+"
from notes import Note
import scales
from scales import Scale
from harmony import RomanNumeral, Chord

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

    def test_fit_to_scale(self) -> None:
        wt = scales.WHOLE_TONE
        rn = RomanNumeral(0).fit_to_scale(wt)
        assert rn == RomanNumeral(0, 'maj', 'aug')
        mx = scales.MIXOLYDIAN
        rn = RomanNumeral(10).fit_to_scale(mx)
        assert rn == RomanNumeral(10, 'maj', 'perf')

    def test_get_scale_chords(self) -> None:
        chords = list(RomanNumeral.get_scale_chords(scales.MIXOLYDIAN))
        assert chords[6] == RomanNumeral(10, 'maj', 'perf')
        chords = list(RomanNumeral.get_scale_chords(scales.WHOLE_TONE))
        assert chords[0] == RomanNumeral(0, 'maj', 'aug')
        assert chords[1] == RomanNumeral(2, 'maj', 'aug')
        chords = list(RomanNumeral.get_scale_chords(scales.HARMONIC_MINOR))
        assert chords[4] == RomanNumeral(7, 'maj', 'perf')

    def test_in_key(self) -> None:
        rn = RomanNumeral(0, 'maj', 'perf')
        assert rn.in_key(Note.from_name('A')) == Chord(Note.from_name('A'), 'maj', 'perf')
        rn = RomanNumeral(7, 'min', 'dim')
        assert rn.in_key(Note.from_name("C")) == Chord(Note.from_name('G'), 'min', 'dim')

class TestChord:
    def test_str(self) -> None:
        ch = Chord(Note.from_name("C"), "min", "dim")
        assert str(ch) == "Cdim"
        ch = Chord(Note.from_name("F"), "maj", "aug", "maj7")
        assert str(ch) == "F+maj7"
        ch = Chord(Note.from_name("D"), "min", "perf", "m7")
        assert str(ch) == "Dm7"
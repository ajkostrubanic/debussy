import re

NOTES_REGEX = re.compile("([ABCDEFG][#]?)([0-9]?)")

NOTES = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]

class Note:
    """Musical note, given by a chroma (the note) and its optional octave."""
    def __init__(self, chroma: int, octave: int = None):
        self.value = (chroma + (octave * 12)) if octave is not None else chroma
        self.name = NOTES[chroma] + (str(octave) if octave is not None else "")
        self.octave = True if octave is not None else False

    def __str__(self) -> str:
        return self.name
    
    def __repr__(self) -> str:
        return f'Note({self.name})'
    
    def __eq__(self, other: 'Note') -> bool:
        if type(other) is Note:
            return self.name == other.name
        return False
    
    def __add__(self, n: int) -> 'Note':
        if self.octave:
            octave = (self.value + n) // 12
            chroma = (self.value + n) % 12
            return Note(chroma, octave)
        else:
            chroma = (self.value + n) % 12
            return Note(chroma)
        
    @classmethod
    def from_name(cls, name: str) -> 'Note':
        """Get a note from its name; e.g, 'A' or 'A#6'."""
        m = NOTES_REGEX.match(name)
        if m.group(2) == "":
            octave = None
            chroma = NOTES.index(m.group(1))
        else:
            octave = int(m.group(2))
            chroma = NOTES.index(m.group(1))
        return Note(chroma, octave)
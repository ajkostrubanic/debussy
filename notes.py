NOTES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

class Note:
    """Musical note, given by a chroma (the note) and its optional octave."""
    def __init__(self, chroma: int, octave: int = None):
        self.value = (chroma + octave * 12) if octave is not None else chroma
        self.name = NOTES[chroma] + (str(octave) if octave is not None else "")
        self.octave = True if octave is not None else False

    def __str__(self) -> str:
        return self.name
    
    def __repr__(self) -> str:
        return f'Note({self.name})'
    
    def __add__(self, n: int) -> 'Note':
        if self.octave:
            octave = (self.value + n) // 12
            chroma = (self.value + n) % 12
            return Note(chroma, octave)
        else:
            chroma = (self.value + n) % 12
            return Note(chroma)
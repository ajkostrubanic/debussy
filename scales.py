from typing import List, Iterator
from notes import Note

class Scale:
    def __init__(self, intervals: List[int]):
        self.intervals = intervals

    def __repr__(self) -> str:
        return f"Scale(intervals={self.intervals})"
    
    def __contains__(self, i: int) -> bool:
        return i in self.intervals

    def in_key(self, root: Note) -> Iterator[Note]:
        for interval in self.intervals:
            yield (root + interval)

MAJOR = Scale([0,2,4,5,7,9,11])
MINOR = Scale([0,2,3,5,7,8,10])
MIXOLYDIAN = Scale([0,2,4,5,7,9,10])
HARMONIC_MINOR = Scale([0,2,3,5,7,8,11])
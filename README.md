# debussy
Music theory command line interface.

## Example
```python
>>> get_roman_numerals(scales.MIXOLYDIAN, note("A"))
['I', 'ii', 'iii+', 'IV', 'v', 'vi', 'VIIb']
['A', 'Bm', 'C#m', 'D', 'Em', 'F#m', 'G']
>>> get_roman_numerals(scales.PHRYGIAN_DOMINANT, note("A")) 
['I', 'IIb', 'III+', 'iv', 'v-dim', 'VIb+', 'viib']
['A', 'A#', 'C#+', 'Dm', 'Edim', 'F+', 'Gm']
>>>
```
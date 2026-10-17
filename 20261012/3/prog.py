import sys
from fractions import Fraction

lines = [l.rstrip('\n') for l in sys.stdin if l.strip()]

h, w = len(lines), len(lines[0])
inside = lines[1:-1]

water = sum(row.count('~') for row in inside)
air = sum(row.count('.') for row in inside)
total = water + air

new_w, new_h = h, w
inner_w = new_w - 2

water_rows = -(-water // inner_w)
air_rows = new_h - 2 - water_rows

print('#' * new_w)
for _ in range(air_rows):
    print('#' + '.' * inner_w + '#')
for _ in range(water_rows):
    print('#' + '~' * inner_w + '#')
print('#' * new_w)

m = max(air, water)
frac_width = max(len(f'{air}/{total}'), len(f'{water}/{total}'))
for ch, v in (('.', air), ('~', water)):
    bar = ch * round(Fraction(v, m) * 20)
    print(bar.ljust(20) + ' ' + f'{v}/{total}'.rjust(frac_width))

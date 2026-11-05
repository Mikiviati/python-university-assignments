from itertools import product
print(*
    filter(
        lambda s: s.count('TOR') == 2,
        map(''.join, product('ORT', repeat=int(input())))
    ),
    sep=', '
)

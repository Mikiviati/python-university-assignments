from decimal import Decimal
from fractions import Fraction


def multiplier(x, y, Type):
    return Type(x) * Type(y)


print(multiplier("5.44", "10.443", Decimal))
print(multiplier("1/6", "1/3", Fraction))
print(multiplier("4.4", "4343434.4333411", float))

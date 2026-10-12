import decimal
from math import factorial


def esum(N, one):
    result = one - one
    if type(one) is decimal.Decimal:
        decimal.getcontext().prec = 100
    for n in range(N):
        result += one / factorial(n)
    return result


print(esum(100, decimal.Decimal("1")))
print(esum(100, float("1")))

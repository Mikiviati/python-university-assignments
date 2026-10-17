from fractions import Fraction

def horner(coeffs, x):
    result = 0
    for a in coeffs:
        result = result * x + a

    return result

def solver(s, w, a_coeffs, b_coeffs):
    b_eval = horner(coeffs=b_coeffs, x=s)
    if b_eval == 0:
        return False

    return horner(coeffs=a_coeffs, x=s) - w * b_eval == 0

input = list(map(Fraction, input().split(',')))
s = input[0]
w = input[1]
deg1 = int(input[2])

a_coeffs = []
for val in input[3:3 + deg1 + 1]:
    a_coeffs.append(val)

b_coeffs = []
for val in input[5+deg1:]:
    b_coeffs.append(val)
    
print(solver(s, w, a_coeffs, b_coeffs))

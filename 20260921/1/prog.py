i = int(input())
s1 = s2 = s3 = "-"
if i % 8 == 0:
    s3 = "+"
if i % 50 == 0:
    s1 = "+"
if i % 2 and i % 25 == 0:
    s2 = "+"
print(f'A {s1} B {s2} C {s3}')

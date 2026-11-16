class A:
    def __init__(self, a):
        self.a = a

    def __add__(self, other):
        return self.__class__(self.a + other.a)

    def __str__(self):
        return f'<{self.a}>'


class B(A):
    pass

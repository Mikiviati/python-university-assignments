from collections import UserString

class DivStr(UserString):

    def __init__(self, seq=""):
        super().__init__(seq)

    def __floordiv__(self, n):
        size = len(self) // n
        return (self[i * size : (i + 1) * size] for i in range(n))

    def __mod__(self, n):
        size = len(self) // n
        return self[n * size :]

if __name__ == "__main__":
    import sys
    exec(sys.stdin.read())

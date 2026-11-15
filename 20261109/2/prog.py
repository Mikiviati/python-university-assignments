from itertools import pairwise

class Triangle:
    def __init__(self, a, b, c):
        self.x1 = a[0]
        self.y1 = a[1]
        self.x2 = b[0]
        self.y2 = b[1]
        self.x3 = c[0]
        self.y3 = c[1]


    def __abs__(self):
        area = abs((self.x2 - self.x1) * (self.y3 - self.y1) -
                   (self.x3 - self.x1) * (self.y2 - self.y1)) / 2

        return 0 if area == 0 else area

    def __bool__(self):
        return abs(self) > 0

    def __lt__(self, other):
        return abs(self) < abs(other)


    def _isinner(self, target):
        def cross(a, b, c):
            return (
                (b[0] - a[0]) * (c[1] - a[1]) -
                (b[1] - a[1]) * (c[0] - a[0])
            )
        
        a, b, c = list(self)[:3]

        d1 = cross(a, b, target)
        d2 = cross(b, c, target)
        d3 = cross(c, a, target)

        return (
            (d1 >= 0 and d2 >= 0 and d3 >= 0) or
            (d1 <= 0 and d2 <= 0 and d3 <= 0)
        )

    def __contains__(self, other):
        if not other:
            return True

        return (
            self._isinner((other.x1, other.y1)) and
            self._isinner((other.x2, other.y2)) and
            self._isinner((other.x3, other.y3))
        )

    def __iter__(self):
        return iter(list((
            (self.x1, self.y1),
            (self.x2, self.y2),
            (self.x3, self.y3),
            (self.x1, self.y1),
        )))

    def __and__(self, other):
        if not self or not other:
            return False

        def cross(a, b, c):
            return (
                (b[0] - a[0]) * (c[1] - a[1]) -
                (b[1] - a[1]) * (c[0] - a[0])
            )

        for t1, t2 in ((self, other), (other, self)):
            a, b, c = list(t1)[:3]
            d = cross(a, b, c)

            vertices = list(t2)[:3]

            for p1, p2 in pairwise(t1):
                signs = [cross(p1, p2, p) for p in vertices]

                if (
                    (d > 0 and all(s < 0 for s in signs)) or
                    (d < 0 and all(s > 0 for s in signs))
                ):
                    return False

        return True

if __name__ == "__main__":
    import sys
    exec(sys.stdin.read())

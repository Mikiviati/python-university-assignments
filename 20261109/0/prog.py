class Rectangle:
    rectcnt = 0

    @property
    def area(self):
        return abs(self.x1 - self.x2) * abs(self.y1 - self.y2)

    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        Rectangle.rectcnt += 1
        setattr(self, f'rect_{Rectangle.rectcnt}', self.rectcnt)

    def __str__(self):
        return (
                f'({self.x1}, {self.y1})'
                f'({self.x1}, {self.y2})'
                f'({self.x2}, {self.y2})'
                f'({self.x2}, {self.y1})'
                f' {self.rectcnt=}'
        )

    def __lt__(self, other):
        return self.area < other.area

    def __eq__(self, other):
        return self.area == other.area

    def __mul__(self, v):
        return Rectangle(self.x1 * v, self.y1 * v, self.x2 * v, self.y2 * v)

    def __rmul__(self, v):
        return self.__mul__(v)

    def __del__(self):
        Rectangle.rectcnt -= 1
        print(f'Rectangle object was deleted, {Rectangle.rectcnt=}')

    def __getitem__(self, index):
        if index == 0:
            return (self.x1, self.y1)
        elif index == 1:
            return (self.x1, self.y2)
        elif index == 2:
            return (self.x2, self.y2)
        elif index == 3:
            return (self.x2, self.y1)
        else:
            raise IndexError(f"Index must be 0, 1, 2, or 3, got {index}")

    def __bool__(self):
        return self.area > 0

    def __iter__(self):
        yield (self.x1, self.y1)
        yield (self.x1, self.y2)
        yield (self.x2, self.y2)
        yield (self.x2, self.y1)

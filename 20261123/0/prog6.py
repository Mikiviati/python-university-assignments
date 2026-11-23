class Counter:
    counter = 0

    def __get__(self, obj, cls):
        return self.counter

    def __set__(self, obj, v):
        self.counter = v


class C:
    counter = Counter()

    def __init__(self):
        self.counter += 1

    def __del__(self):
        self.counter -= 1

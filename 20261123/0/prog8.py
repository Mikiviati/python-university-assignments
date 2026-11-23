from string import ascii_letters


class Slotter:
    __slots__ = ascii_letters


class Trad:
    def __init__(self):
        for attr in ascii_letters:
            setattr(self, attr, attr)


def get_set_delete(obj):
    obj.x = 'val'
    obj.x
    del obj.x


def test_T():
    get_set_delete(Trad())


def test_S():
    get_set_delete(Slotter())

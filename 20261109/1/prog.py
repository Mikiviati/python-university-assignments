class Omnibus:
    _counts = {}

    def __init__(self):
        object.__setattr__(self, '_my_attrs', set())

    def __setattr__(self, name, value):
        if name.startswith('_'):
            object.__setattr__(self, name, value)
        else:
            if name not in self._my_attrs:
                self._my_attrs.add(name)
                Omnibus._counts[name] = Omnibus._counts.get(name, 0) + 1

    def __getattr__(self, name):
        if name.startswith('_'):
            return object.__getattribute__(self, name)
        return Omnibus._counts.get(name, 0)

    def __delattr__(self, name):
        if name.startswith('_'):
            object.__delattr__(self, name)
        else:
            if name in self._my_attrs:
                self._my_attrs.remove(name)
                if Omnibus._counts.get(name, 0) > 0:
                    Omnibus._counts[name] -= 1

if __name__ == "__main__":
    import sys
    exec(sys.stdin.read())


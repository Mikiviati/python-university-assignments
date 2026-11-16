def init(self):
    __init__(self, a):
        self.a = a

Base = type("Base", (), {"__init__": lambda self, a: setattr(self, "__a", a), "__str__": 'fff'})
Derrived = type("D", (Base,), {})



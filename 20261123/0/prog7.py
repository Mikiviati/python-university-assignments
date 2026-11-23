class C:
    _age = 100

    @property
    def age(self):
        if self._age == 42:
            print("secret value!")
            return -1
        return self._age

    @age.setter
    def age(self, val):
        if val <= 128:
            self._age = val
        else:
            raise ValueError("too old!")




class Base:
    def __init__(self) -> None:
        self._a = 20


class Derived(Base):
    def __init__(self) -> None:
        super().__init__()

    def call(self):
        print(self._a)
der = Derived()
print(der.call())
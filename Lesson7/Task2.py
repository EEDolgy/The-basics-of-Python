from abc import ABC, abstractmethod

class Clothes(ABC):
    @abstractmethod
    def tissue_calc(self):
        pass

class Coat(Clothes):
    def __init__(self, v):
        self.v = v

    @property
    def property(self):
        return self.v

    def tissue_calc(self):
        return round(self.v/6.5 + 0.5, 2)

class Suit(Clothes):
    def __init__(self, h):
        self._h = h

    @property
    def h(self):
        return self._h

    def tissue_calc(self):
        return round(2 * self.h + 0.3, 2)

item = Coat(5)
print(item.property)
print(item.tissue_calc())
item2 = Suit(7)
print(item2.h)
print(item2.tissue_calc())
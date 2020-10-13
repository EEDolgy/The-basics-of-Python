import time
from itertools import cycle

class Trafficklight:
    def running(self):
        for el in cycle([('red', 7), ('yellow', 2), ('green', 5)]):
            self.__color = el[0]
            print(self.__color)
            time.sleep(el[1])

traf = Trafficklight()
traf.running()
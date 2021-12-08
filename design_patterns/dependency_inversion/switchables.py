from abc import ABC, abstractmethod


class Switchable(ABC):

    @abstractmethod
    def switch_on(self):
        pass

    @abstractmethod
    def switch_off(self):
        pass

class LightBulb(Switchable):
    def switch_on(self):
        print('Turning bulb on')

    def switch_off(self):
        print('Turning bulb off')

class Fan(Switchable):
    def switch_on(self):
        print('Turning Fan on')

    def switch_off(self):
        print('Turning Fan off')



from design_patterns.dependency_inversion.switchables import Switchable, LightBulb


class ElectricPowerSwitch:
    def __init__(self, switchable: Switchable):
        self.switchable = switchable
        self.on = False

    def press(self):
        if self.on:
            self.switchable.switch_off()
            self.on = False
        else:
            self.switchable.switch_on()
            self.on = True


if __name__ == '__main__':
    power_switch = ElectricPowerSwitch(LightBulb())
    power_switch.press()
    power_switch.press()
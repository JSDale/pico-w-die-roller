import time
from gfx_pack import GfxPack, SWITCH_A, SWITCH_B, SWITCH_C, SWITCH_D, SWITCH_E
import random

class DieRoller:

    def __init__(self):
        self.set_up()

    def clear(self):
        self.display.set_pen(0)
        self.display.clear()
        self.display.set_pen(self.pen_size)

    def roll(self, lowest, highest):
        number = random.randint(lowest, highest)
        return number

    def display_roll(self, rolls):
        print(f"{self.lowest}, {self.highest}")
        for i in range(rolls):
            number = self.roll(self.lowest, self.highest)
            self.clear()
            self.display.text(f"{number}", int(self.width/2)-self.pen_size, int(self.height/2)-self.pen_size, 0, 5)
            self.display.update()
            time.sleep(0.2)

    def set_die_type(self, upper_value):
        self.highest = upper_value
        self.clear()
        self.display.text(f"D{self.highest}", 0, 0, self.width, 4)
        self.display.update()

    def set_up(self):
        self.lowest = 1
        self.highest = 6
        self.pen_size = 15
        self.width = 0
        self.height = 0

        self.gp = GfxPack()
        self.display = self.gp.display

        self.width, self.height = self.display.get_bounds()
        self.display.set_backlight(0)
        self.display.set_font("bitmap8")

        self.gp.set_backlight(0, 0, 0, 125)
        self.clear()
        self.display.set_pen(self.pen_size)
        self.display.text("Set at 1 - 6", 0, 40, self.width, 2)
        self.display.text("Press A to roll", 0, 0, self.width, 2)
        self.display.update()
        
    def main(self):
        while True:
            if self.gp.switch_pressed(SWITCH_A):                       
                self.display_roll(5)
            elif self.gp.switch_pressed(SWITCH_B):
                self.set_die_type(6)
            elif self.gp.switch_pressed(SWITCH_C):
                self.set_die_type(12)
            elif self.gp.switch_pressed(SWITCH_D):
                self.set_die_type(20)
            elif self.gp.switch_pressed(SWITCH_E):
                time.sleep(1)
            time.sleep(0.01)

dr = DieRoller()
dr.main()

import time
from gfx_pack import GfxPack, SWITCH_A, SWITCH_B, SWITCH_C, SWITCH_D, SWITCH_E
import random

lowest = 1
highest = 6

gp = GfxPack()
display = gp.display

WIDTH, HEIGHT = display.get_bounds()
display.set_backlight(0)  # turn off the white component of the backlight


# sets up a handy function we can call to clear the screen
def clear():
    display.set_pen(0)
    display.clear()
    display.set_pen(15)


# set up
display.set_font("bitmap8")

gp.set_backlight(0, 0, 0, 125)
clear()
display.set_pen(15)
display.text("Press A to roll", 0, 0, WIDTH, 2)
display.update()

while True:
    if gp.switch_pressed(SWITCH_A):                       # if a button press is detected...                                          # clear to black
        gp.set_backlight(255, 0, 0, 0)                    # red, green, blue, white
        clear()
        display.text("Button A pressed", 0, 0, WIDTH, 2)  # display some text on the screen
        display.update()                                  # update the display
        time.sleep(0.2)
    elif gp.switch_pressed(SWITCH_B):
        gp.set_backlight(255, 125, 0, 0)
        clear()
        display.text("Button B pressed", 0, 0, WIDTH, 2)
        display.update()
        time.sleep(0.2)
    elif gp.switch_pressed(SWITCH_C):
        gp.set_backlight(0, 255, 0, 0)
        clear()
        display.text("Button C pressed", 0, 0, WIDTH, 2)
        display.update()
        time.sleep(0.2)
    elif gp.switch_pressed(SWITCH_D):
        gp.set_backlight(0, 0, 255, 0)
        clear()
        display.text("Button D pressed", 0, 0, WIDTH, 2)
        display.update()
        time.sleep(0.2)
    elif gp.switch_pressed(SWITCH_E):
        gp.set_backlight(255, 0, 255, 0)
        clear()
        display.text("Button E pressed", 0, 0, WIDTH, 2)
        display.update()
        time.sleep(1)
    time.sleep(0.01)  # this number is how frequently the Pico checks for button presses

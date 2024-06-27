# Program to create a virtual die that uses gestures to roll and
# display the die value on the LED display
# EPIC 2022
# Paul Hummel

from microbit import *
import urandom

#pin0.set_touch_mode(pin0.CAPACITIVE)
pin1.set_touch_mode(pin1.CAPACITIVE)
pin2.set_touch_mode(pin2.CAPACITIVE)
pin_logo.set_touch_mode(pin_logo.CAPACITIVE)

# Code in a 'while True:' loop repeats forever
while True:
    if (accelerometer.was_gesture('shake')):
        for roll in range(5):
            for die in range(1,7):
                display.show(die)
                sleep(roll*20+50)
        number = urandom.randrange(1,7)
        display.show(number)
    sleep(100)




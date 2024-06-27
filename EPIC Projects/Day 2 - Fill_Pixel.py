# Program that randomly turns on LEDs on the display. Shaking the
# micro:bit will clear all of the LEDs and start the process over
# EPIC 2022
# Paul Hummel

from microbit import *
import urandom

# Code in a 'while True:' loop repeats forever
while True:
    #fill in the display, 1 pixel at a time randomly    
    x = urandom.randrange(0,5)
    y = urandom.randrange(0,5)
    display.set_pixel(x,y,9)
    sleep(100)
    if (accelerometer.was_gesture('shake')):
        display.clear()
        sleep(100)



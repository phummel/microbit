# Program that randomly brightens LEDs on the LED display until they
# are each at full brightness. Shaking the micro:bit will clear all
# of the LEDs and start the process over
# EPIC 2022
# Paul Hummel

from microbit import *
import urandom

# Code in a 'while True:' loop repeats forever
while True:
    #randomly turn on 1 pixel at a time
    x = urandom.randrange(5)             #random pixel
    y = urandom.randrange(5)
    brightness = display.get_pixel(x,y)  #get brightness
    brightness = brightness + 3          #increase bright
    if (brightness > 9):                 #check not over 9
        brightness = 9
    display.set_pixel(x,y,brightness)    #update pixel
    sleep(50)
    if (accelerometer.is_gesture('shake')):
        display.clear()
        sleep(200)

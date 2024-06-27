# Reads each axis of the accelerometer and print each value separately
# on the LED display
# GenCyber Camp 2021
# Paul Hummel

from microbit import *

while True:
    if pin_logo.is_touched() :
        display.scroll("X: "+str(accelerometer.get_x()))
        display.scroll("Y: "+str(accelerometer.get_y()))
        display.scroll("Z: "+str(accelerometer.get_z()))
        sleep(100)
    sleep(100)

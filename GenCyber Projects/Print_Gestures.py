# Program that reads gestures from the accelerometer and prints
# them to the LED display
# GenCyber Camp 2021
# Paul Hummel

from microbit import *

while True:
    if pin_logo.is_touched() :
        gestures = accelerometer.get_gestures()
        display.scroll(len(gestures))
        sleep(10)
        for name in gestures :
            display.scroll(name)
            sleep(10)
    sleep(100)

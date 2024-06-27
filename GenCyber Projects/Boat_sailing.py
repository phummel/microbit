# Program that creates a boat image on the LED display
# and moves the image left and right to simulate motion
# GenCyber Camp 2021
# Paul Hummel

from microbit import *

boat = Image("00000:"
              "05050:"
              "05050:"
              "99999:"
              "09990")

while True:
    for i in range(11):
        display.show(boat.shift_left(i-5))
        sleep(200)
    for i in range(11):
        display.show(boat.shift_right(i-5))
        sleep(200)

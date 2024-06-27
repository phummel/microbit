# Program to create a whistle sound
# GenCyber Camp 2021
# Paul Hummel

from microbit import *
import music

while True:
    for i in range(5, 10000, 50):
        music.pitch(i)
        sleep(10)
    sleep(2000)

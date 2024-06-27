# Create a magic 8 ball that works by shaking the micro:bit and
# answer is displayed on the LED display
# EPIC 2022
# Paul Hummel

from microbit import *
import urandom

answer_list = ["Yes","No","Maybe","Ask again later", "Outlook Hazy"]

# Code in a 'while True:' loop repeats forever
while True:
    display.show(8)
    if (accelerometer.is_gesture('shake')):
        answer = urandom.randrange(len(answer_list))
        display.scroll(answer_list[answer])
        sleep(100)
    sleep(100)


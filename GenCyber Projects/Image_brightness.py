# Create a flashlight that has an automatic brightness
# adjustment that gets dimmer when the envrionment is
# dark and brighter when it is light outside
# GenCyber Camp 2021
# Paul Hummel

from microbit import *

light_on = False                    # default light to off
flash_light = Image()               # create a blank image
flash_light.fill(9)                 # fill blank image with brightness value
       
if (flash_light.get_pixel(0,0) >= 9) :
    flash_light = flash_light / 10
elif (flash_light.get_pixel(0,0) >= 5) :
    flash_light = flash_light * 1.1
elif (flash_light.get_pixel(0,0) >= 3) :
    flash_light = flash_light * 1.3
else :
    flash_light = flash_light * 1.5
    

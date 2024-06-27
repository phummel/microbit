# Progrma that reads a line from the serial terminal and prints
# it to the LED display whenever return is entered
# GenCyber Camp 2021
# Paul Hummel

from microbit import *

#initialize serial terminal
uart.init(115200)
#https://googlechromelabs.github.io/serial-terminal/

text = ""

uart.write("\x1B\x5B2J")     #clear the terminal
uart.write("\x1B\x5BH")
uart.write("Enter text to display: ")
            

while True:
    if uart.any() == True :             #check if uart has anything in buffer
        char = uart.read()              #read from uart buffer
        uart.write(char)                #echo character to terminal
        char = str(char, 'UTF-8')       #convert to character
        if (char == '\r'):              #return character
            display.scroll(text, loop=True, wait=False)
            uart.write("\x1B\x5B2J")    #clear the terminal
            uart.write("\x1B\x5BH")
            uart.write("Enter text to display: ")
            text = ""
        else:
            text += char                #add character to text

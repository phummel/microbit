# micro:bit program that creates a lockbox that can only be unlocked with
# the correct password. Passcodes are entered via serial terminal. The
# state of the lockbox is displayed with LEDs
# GenCyber Camp 2021
# Paul Hummel

from microbit import *
import speech

lock = Image("09990:"
             "90009:"
             "99999:"
             "90009:"
             "99999")
             
unlock = Image("09990:"
             "90009:"
             "90000:"
             "99999:"
             "99999")

def reset_lock():
    uart.write("\x1B\x5B2J")     #clear the terminal
    uart.write("\x1B\x5BH")
    uart.write("Enter the Passcode: ")
    display.show(lock)

#initialize serial terminal
uart.init(baudrate=9600, bits=8, parity=None, stop=1)

reset_lock()
passcode = ''
    
while True:
    if uart.any() == True :             #check if uart has anything in buffer
        char = uart.read()              #read from uart buffer
        char = str(char, 'UTF-8')       #convert to character
        uart.write(char)                #echo character to terminal
        if (char != '\r') :
            passcode = passcode + char  #not return add to passcode
        else :
            if (passcode == "drwho") :
                display.show(unlock)
                uart.write("\r\n\r\nYou Found the Passcode!")
                speech.say("Congratulations",  speed=92, pitch=60, throat=190, mouth=190)
                uart.write("\r\nPress any key to relock the system")
                while (uart.any() != True) : #wait for any key press
                    pass
                char = uart.read()           #clear uart buffer of key press
                reset_lock()
                passcode = ''
            else :
                display.show(Image.SAD)
                uart.write("\r\n\r\nPasscode incorrect")
                speech.say("You have failed", speed=120, pitch=100, throat=100, mouth=200)
                sleep(4000)
                passcode = ''
                reset_lock()
    
    if (accelerometer.current_gesture() == "shake") :
        display.show(Image.ANGRY)
        speech.say("You cannot break in that way", speed=120, pitch=100, throat=100, mouth=200)
        sleep(2000)
        display.show(lock)
    
        

# Program that will encrypt a string of text using a Caesar cipher
# Text is entered and displayed using serial terminal
# GenCyber Camp 2021
# Paul Hummel

from microbit import *

def uart_clear():
    uart.write("\x1B\x5B2J")     #clear the terminal
    uart.write("\x1B\x5BH")

def uart_readline():
    command = ""
    while True:
        if (uart.any() == True):            #check if anything in uart buffer
            char = uart.read()              #read a character from buffer
            char = str(char, 'UTF-8')       #convert to character
            if (char == "\r"):
                return command
            else:
                uart.write(char)            #echo character to terminal
                command += char

def caesar(plain_text, shift):
  """ Converts text using a Caesar Cipher
  
  Arguments: plan_text is an input text string
             shift is a number (1-25) specifying shift amount
  
  Returns: cipher text shifted by specified amount
  
  """
  plain_text = plain_text.lower()   #convert text to lowercase
  result = ""
  # transverse the plain text
  for letter in text:
    if (letter == " "):             # skip spaces
        result += letter
    else:                           #shift character by number
        result += chr((ord(letter)-97 + shift) % 26 + 97)
  return result

#initialize serial terminal
uart.init(115200)

while True:
    uart_clear()
    uart.write("Enter text to display: ")
    text = uart_readline()
    ### Perform Caesar Cipher on text
    for i in range(1,26):
        uart.write("\n\r")
        uart.write(str(i)+" : "+caesar(text,i))
    #wait for key press
    while(uart.any() == False):
        continue
    uart.read() #clear the key press from uart buffer

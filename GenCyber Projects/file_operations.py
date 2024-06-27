# Demo program that can create a file with 1 line of text
# When creating a file, checks for existing files and
# will print out the file
# GenCyber Camp 2021
# Paul Hummel

from microbit import *
import os

def os_check_file(filename):
    """Checks if a specific filename exists, returning True or False
       
    Arguments: filename: text string of file name to read
    """
    filelist = os.listdir()         #get a list of all files
    try:
        filelist.index(filename)    #if name doesn't exist, causes exception
        return True
    except:
        return False

def read_file(filename):
    """Reads a single line of text from a file and prints it to uart If the
    file does not exist, an error code is printed to uart
       
    Arguments: filename: text string of file name to read
    """
    if (os_check_file(filename)):       #verify file exists
        pass_file = open(filename,"r")  #open file
        password = pass_file.readline() #read first line
        pass_file.close()               #close file (never forget!)
        uart.write(password)            #print line from file
        uart.write("\r\n")
    else:
        uart.write(filename+" does not exist\r\n")

def write_file(filename, text):
    """writes a single line of text to a file. If the file exists,
    it is overwritten.
       
    Arguments: filename: text string of file name to write
               text    : string of text to write to the file
    """
    pass_file = open(filename,"w")  #open file
    pass_file.write(text)           #write text
    pass_file.close()               #close file (never forget!)

def uart_read_line():
    """Reads a line of text from uart, echoing each character to uart until a
    return (\r) is entered. The \r is not echoed or included in the string
    returned
    
    Returns: text_line: a text string of the characters read
    """
    text_line = ""
    while True:
        if (uart.any() == True):            #check if anything in uart buffer
            letter = uart.read()            #read a character from buffer
            letter = str(letter, 'UTF-8')   #convert to character
            if (letter == "\r"):
                return text_line
            else:
                uart.write(letter)          #echo character to terminal
                text_line += letter

def uart_clear():
    """Clears the uart terminal and resets cursor to the top left position
    """
    uart.write("\x1B\x5B2J")
    uart.write("\x1B\x5BH")

uart.init(115200)

while True:
    uart.write("Enter a filename: ")
    filename = uart_read_line()
    
    if (os_check_file(filename)):
        uart.write("\n\r"+filename+" exists!\r\n")
        read_file(filename)
    else:
        uart.write("\n\r"+filename+" does not exist\r\n")
        uart.write("Enter a new text string: ")
        file_text = uart_read_line()
        write_file(filename,file_text)
        uart.write("\r\n")
    

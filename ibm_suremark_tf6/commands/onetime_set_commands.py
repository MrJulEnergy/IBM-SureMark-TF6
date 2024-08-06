import serial
from PIL import Image
from ibm_suremark_tf6.base import Printer
import time

def download_graphics(printer: Printer, filepath: str, logo_number: int):
    # TODO: Dont erase the EEPROM if logo_number is free
    assert logo_number <= 40
    def bmp_to_bytes(filepath):
        img = Image.open(filepath)
        img = img.convert("1")
        
        width, height = img.size

        assert width <= 8*72 and height <= 8*255
        assert width % 8 == 0 and height % 8 == 0

        binary_string = ""
        for y in range(height):
            for x in range(width):
                pixel = img.getpixel((x, y))
                binary_string += "1" if pixel == 0 else "0"

        num = int(binary_string, 2) # Binary to int
        data = num.to_bytes(int(len(binary_string)/8), byteorder="big")
        
        return data, width, height
    data, width, height = bmp_to_bytes(filepath)
    
    with serial.Serial(printer.port, printer.baudrate, timeout=printer.timeout) as ser:
        ser.write(b"\x1B\x23\x01") # Clear sector
        time.sleep(1) # TODO Check if EEPROM is erased
        ser.write(b"\x1D\x2A"+logo_number.to_bytes()+int(width/8).to_bytes()+int(height/8).to_bytes()+data) # load data
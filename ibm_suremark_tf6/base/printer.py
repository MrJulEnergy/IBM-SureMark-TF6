import serial
import binascii

class Printer:
    def __init__(self, port: str = "/dev/ttyUSB0", baudrate: int = 9600, timeout: float = 5):
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout

import serial
from ibm_suremark_tf6.base import Printer


def cut_paper(printer: Printer):
    with serial.Serial(printer.port, printer.baudrate, timeout=printer.timeout) as ser:
        ser.write(b"\x1B\x6D")

def reset(printer: Printer):
    with serial.Serial(printer.port, printer.baudrate, timeout=printer.timeout) as ser:
        ser.write(b"\x10\x05\x40")
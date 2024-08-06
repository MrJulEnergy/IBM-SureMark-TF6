import serial
from ibm_suremark_tf6.base import Printer


def print_barcode(printer: Printer, typ: int , data: int) -> None:
    """
    Barcode Types:
    0 UPC-A
    1 UPC-E
    2 JAN 13 (EAN-13)
    3 JAN8 (EAN-8)
    4 CODE 39
    5 ITF
    6 CODABAR
    7 CODE 128C
    8 CODE 93
    9 CODE 128A, 128B, and 128C (This command is not supported for Models Til and TI2.)

    data: 
    For n=00 through n=08, the ASCII representation of the characters to be printed.
    For n=09, the hexadecimal representation of the characters to be printed.
    The first byte of data must be the byte-count of the remaining data. 
    The trailing X'00' should not be included for this command.
    """
    with serial.Serial(printer.port, printer.baudrate, timeout=printer.timeout) as ser:
        # TODO
        pass

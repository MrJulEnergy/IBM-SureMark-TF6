import serial
from ibm_suremark_tf6.base import Printer


def hold_buffer(printer: Printer) -> None:
    with serial.Serial(printer.port, printer.baudrate, timeout=printer.timeout) as ser:
        ser.write(b"\x1B\x37")
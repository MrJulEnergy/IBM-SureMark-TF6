import serial
from ibm_suremark_tf6.base import Printer


def print_logo(printer: Printer, logo_number: int, dot_density: int) -> None:
    assert 1 <= logo_number <= 40
    assert 0 <= dot_density <= 2
    with serial.Serial(printer.port, printer.baudrate, timeout=printer.timeout) as ser:
            ser.write(b"\x1D\x2F"+dot_density.to_bytes()+logo_number.to_bytes())
            print((b"\x1D\x2F"+dot_density.to_bytes()+logo_number.to_bytes()).hex("-"))

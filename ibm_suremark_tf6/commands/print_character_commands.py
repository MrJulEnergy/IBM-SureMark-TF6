"""These commands should be sent after ASCII data is sent to the printer 
and is being held in the print buffer. 
Any of these commands will increment the line count by 1. 
(See “Status byte 6” on page 186 and “Reset line count” on page 176)
"""

import serial
from ibm_suremark_tf6.base import Printer


def print_and_linefeed(printer: Printer, typ: str = "LF") -> None:
    # Print the data in the print buffer and fedds the paper by a preset amount
    with serial.Serial(printer.port, printer.baudrate, timeout=printer.timeout) as ser:
        if typ == "LF": # Line Feed
            ser.write(b"\x0A")
            return
        if typ == "CR": # Carrige Return
            # TODO: There is an MCT to enable or disable this command. The default is to disable or ignore the CR command.
            ser.write(b"\x0D")
            return
        else:
            raise Exception("From Type for print_and_linefeed")

def print_form_feed_and_cut(printer: Printer) -> None:
     """Prints data in the print buffer and feeds the paper in the customer
        receipt station or document insert station by a preset amount, 
        until the document exits the feed rollers. If a cutter is available 
        at the station (CR station only), it cuts the paper.
        """
     with serial.Serial(printer.port, printer.baudrate, timeout=printer.timeout) as ser:
        ser.write(b"\x0C")

def feed_paper(printer: Printer, n_lines: int):
    with serial.Serial(printer.port, printer.baudrate, timeout=printer.timeout) as ser:
        ser.write(b"\x1B\x64"+n_lines.to_bytes())


def send(printer: Printer, msg: str) -> None:
    with serial.Serial(printer.port, printer.baudrate, timeout=printer.timeout) as ser:
            ser.write(bytearray(msg, encoding="ascii"))

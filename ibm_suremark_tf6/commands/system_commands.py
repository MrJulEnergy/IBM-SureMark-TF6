import serial
from ibm_suremark_tf6.base import Printer


def exercise_program(printer: Printer) -> None:
    with serial.Serial(printer.port, printer.baudrate, timeout=printer.timeout) as ser:
        ser.write(b"\x1B\x78")
    
def status_request(printer: Printer) -> list:
    from ibm_suremark_tf6.static import status
    with serial.Serial(printer.port, printer.baudrate, timeout=printer.timeout) as ser:
        ser.write(b"\x1B\x76")
        msg_len = int.from_bytes(ser.read(2))- 2 # first two bytes are the length of the message
        raw_msg = ser.read(msg_len).hex()
        msg = [bin(int(raw_msg[i:i+2], 16))[2:].zfill(8) for i in range(0, len(raw_msg), 2)] # seperated into 8 bit values
        report = {}
        for i in range(len(msg)):
            if i == 5:
               # line count
               continue
            if i == 3:
                # TODO Contains the printer engineering code (EC) level with all status messages.
                continue
            if i > 7:
                # TODO Either 5 bytes of additional status from the “Extended address command-request printer ID” on page 112 command, or up to 246 bytes of user data
                continue
            else:
                byte_report = []
                for j in range(len(msg[1])-1, -1, -1):
                    if int(msg[i][j]):
                        try:
                            byte_report.append(status[i][7-j])
                        except Exception:
                            pass
                report[i] = byte_report
        return report


def extended_addres_command_request(printer: Printer):
    # TODO
    # Does the same as status_request() but sends 5 additional bits
    # Manal Page 112
    pass

def verify_previous_commands(printer: Printer):
    # TODO
    # Don't know yet how this works (Manual Page 111)
    pass
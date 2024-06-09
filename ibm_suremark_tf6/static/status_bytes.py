byte_one_status_dict = {
    0: "Command complete (immediate command and flash storage commands). Set to 1 when the command is complete, except for “Erase flash EPROM sector on page 123, for which it is set to 1 when the command is sent. (See bit 7 of “Status byte 3” on page 185)",
    1: "Cash receipt right home position. Set to 1 when the print head is in the customer receipt right home position.",
    2: "Left home position Set to 1 when the print head is in the left home position.",
    3: "Document right home position. Set to 1 when the print head is in the document right home position.",
    4: "Reserved. Always 0.",
    5: "Ribbon cover open. Set to 1 when the ribbon cover is open.",
    6: "Cash receipt print error. Paper cover is open, the customer receipt station is out of paper, or the cutter is jammed in the closed position.",
    7: "Command reject.",
}
byte_two_status_dict = {
    0: "Document ready. Set to 0 when the document insert station is ready for printing. This occurs when both document sensors detect the document and the document has been fed to the first print position.",
    1: "Document present under the front sensor. Set to 0 when a document is under the front document sensor.",
    2: "Document present under the top sensor. Set to 0 when a document is under the top document sensor.",
    3: "Reserved. Always equals 1.",
    4: "Print buffer held. Set to 1 when the print buffer is being held. Cleared when buffer released.",
    5: "Open throat position. Set to 1 when the print head is in the open throat position.",
    6: "Buffer empty. Set to 1 when no print data and no commands are in the buffer.",
    7: "Buffer Full. Set when only IK bytes are available in the buffer.",
}
byte_three_status_dict = {
    0: "Memory sector is full.",
    1: "Home error.",
    2: "Document error. The document was not inserted after the document station was selected, and the wait subsequently timed out.",
    3: "Flash EPROM load error or MCT load error.",
    4: "Reserved. Always equals 0.",
    5: "User flash storage sector is full.",
    6: "Firmware error. CRC on the firmware failed. The printer is running out of the boot sector. Only system commands and firmware commands are accepted.",
    7: "Command complete (“Erase flash EPROM sector” on page 123, “Flip check” on page 166, and whenever a physical line is printed). Set to 1 when the command is complete or a physical line is printed.",
}

byte_four_status_dict = {}

byte_five_status_dict = {
    0: "Printer ID Request/Extended Address command. Set to 1 when responding to a Printer ID request.",
    1: "EC Level. Set to 1 when responding to an EC level request.",
    2: "MICR Read. Set to 1 when responding to a MICR read command.",
    3: "MCT Read. Set to 1 when responding to an MCT read command.",
    4: "User flash read. Set to 1 when responding to a flash read command.",
    5: "Reserved. Defaults to 1",
    6: "Scan Complete. Set to 1 when scan completed successfully.",
    7: "Set to 1 when responding to a 'Retrieve scanned image' command.",
}

byte_six_status_dict = {}

byte_seven_status_dict = {
    0: "Reserved.",
    1: "Reserved.",
    2: "Reserved.",
    3: "Cash drawer status (0 if cash drawer status (port pin 3) at ground.",
    4: "Print key pressed (1 = pressed).",
    5: "Reserved. Defaults to 1",
    6: "Station selected. Set to 1 when document insert station is selected.",
    7: "Document feed error. Set when there is an error after a MICR read command or a flip check command is executed.",
}

byte_eight_status_dict = {
    0: "Reserved.",
    1: "Reserved.",
    2: "Reserved.",
    3: "Reserved.",
    4: "Reserved (always 0).",
    5: "Reserved.",
    6: "Reserved.",
    7: "Thermal print head or motor is almost too hot to continue printing. This bit is set to ON when the printer determines that the print head or motor are getting close to the point where the printer must slow down to keep from overheating the station. This is only supported on Models TI8/TG8 and TI9/TG9.",
}

status = [byte_one_status_dict, byte_two_status_dict, byte_three_status_dict, byte_four_status_dict, byte_five_status_dict, byte_six_status_dict, byte_seven_status_dict, byte_eight_status_dict]
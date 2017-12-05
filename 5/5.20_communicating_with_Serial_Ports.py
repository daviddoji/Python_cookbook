#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 19:56:23 2017

@author: david
"""

import serial

"""
Problem
-------
You want to read and write data over a serial port, typically to interact
with some kind of hardware device (e.g., a robot or sensor).
"""

ser = serial.Serial('/dev/tty.usbmodem641', baudrate=9600, bytesize=8,
                    parity='N', stopbits=1)

# read and write data
ser.write(b'G1 X50 Y50\r\n')
resp = ser.readline()

import serial
import time

ser = serial.Serial("/dev/ttyAMA2")
ser.baudrate = 115200

while True:
    print('Received Bytes: ', ser.read_all())
    time.sleep(1)
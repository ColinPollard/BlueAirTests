import serial
import time

ser = serial.Serial("/dev/ttyAMA2")
ser.baudrate = 115200

while True:
    print('Sending: Test')
    ser.write("Test\n")
    received = ser.readline()
    print('Received: ', received)
    time.sleep(1)
    
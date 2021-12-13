import serial
import datetime
import time

with serial.Serial(port='COM8', baudrate=9600, bytesize=8, parity='N', stopbits=1, timeout=1.0) as sdev:
    sdev.write(b'*IDN?\n')
    print(sdev.readline().decode('utf-8').strip())
    sdev.write(b'VSET1:24.1\n')
    sdev.write(b'VSET1?\n')
    print('Set: {} volts'.format(sdev.readline().decode('utf-8').strip()))
    sdev.write(b'ISET1:0.4\n')
    sdev.write(b'ISET1?\n')
    print('Set: {} Amps'.format(sdev.readline().decode('utf-8').strip()))
    sdev.write(b'OUT1\n')   # Turn on if not already
    for i in range(1000):
        sdev.write(b'VSET1:30.1\n')
        sdev.write(b'VSET1?\n')
        print('{}, Count: {}, Set: {} volts'.format(datetime.datetime.now(), i, sdev.readline().decode('utf-8').strip()))
        time.sleep(300)
        sdev.write(b'VSET1:24.1\n')
        sdev.write(b'VSET1?\n')
        print('{}, Count: {}, Set: {} volts'.format(datetime.datetime.now(), i, sdev.readline().decode('utf-8').strip()))
        time.sleep(120)

'''Test the voltage doubler'''
import datetime
import time
import serial

sequence = [{'time_s':1.0, 'voltage':12.0},
            {'time_s':1.0, 'voltage':13.0},
            {'time_s':1.0, 'voltage':14.0},
            {'time_s':1.0, 'voltage':15.0},
            {'time_s':1.0, 'voltage':16.0},
            {'time_s':1.0, 'voltage':17.0},
            {'time_s':1.0, 'voltage':18.0},
            {'time_s':1.0, 'voltage':8.0},
            {'time_s':1.0, 'voltage':9.0},
            {'time_s':1.0, 'voltage':10.0},
            {'time_s':1.0, 'voltage':11.0}
            ]

with serial.Serial(port='COM11', baudrate=9600, bytesize=8, parity='N', stopbits=1, timeout=1.0) as sdev:
    sdev.write(b'*IDN?\n')
    print(sdev.readline().decode('utf-8').strip())
    sdev.write(b'VSET1:12.0\n')
    sdev.write(b'VSET1?\n')
    set_voltage = sdev.readline().decode('utf-8').strip()
    sdev.write(b'ISET1:5.0\n')
    sdev.write(b'ISET1?\n')
    print('Set: {} volts, {} Amps'.format(set_voltage, sdev.readline().decode('utf-8').strip()))
    sdev.write(b'OUT1\n')   # Turn on if not already

    for i in range(100):
        for step in sequence:
            sdev.write('VSET1:{:.1f}\n'.format(step['voltage']).encode('utf-8'))
            sdev.write(b'VSET1?\n')
            set_voltage = sdev.readline().decode('utf-8').strip()
            print('Set: {} volts for {} seconds'.format(set_voltage, step['time_s']))
            time.sleep(step['time_s'])

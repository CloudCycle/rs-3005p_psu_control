'''Test the voltage doubler'''
import time
from msvcrt import kbhit
import serial

delay_s = 0.02
vset = 25
iset = 15

with serial.Serial(port='COM6', baudrate=9600, bytesize=8, parity='N', stopbits=1, timeout=1.5) as sdev:
    sdev.write(b'*IDN?\n')
    print(sdev.readline().decode('utf-8').strip())
    sdev.write('VSET:{:.1f}\n'.format(vset).encode('utf-8'))
    sdev.write(b'VSET?\n')
    set_voltage = sdev.readline().decode('utf-8').strip()
    sdev.write('ISET:{:.1f}\n'.format(iset).encode('utf-8'))
    sdev.write(b'ISET?\n')
    print('Set: {} volts, {} Amps'.format(set_voltage, sdev.readline().decode('utf-8').strip()))

    #TODO this line does not work for 72 series
    sdev.write(b'OUT\n')   # Turn on if not already

    while True:
        try:
            sdev.write('VSET:{:.1f}\n'.format(vset).encode('utf-8'))
            time.sleep(delay_s)
            sdev.write('VSET:{:.1f}\n'.format(0).encode('utf-8'))
            time.sleep(delay_s)
        except Exception:
            exit()

        if kbhit():
            break

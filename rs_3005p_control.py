import serial
import datetime
import time

time_at_30v_s = (60*2) # Enough time to detect the higher voltage and get into measurement mode
time_at_24v_s = (60*7) # Devices set to 5 minutes before entering idle after 24 V detected

with serial.Serial(port='/dev/ttyACM0', baudrate=9600, bytesize=8, parity='N', stopbits=1, timeout=1.0) as sdev:
    sdev.write(b'*IDN?\n')
    print(sdev.readline().decode('utf-8').strip())
    sdev.write(b'VSET1:24.1\n')
    sdev.write(b'VSET1?\n')
    print('Set: {} volts'.format(sdev.readline().decode('utf-8').strip()))
    sdev.write(b'ISET1:1.6\n')
    sdev.write(b'ISET1?\n')
    print('Set: {} Amps'.format(sdev.readline().decode('utf-8').strip()))
    sdev.write(b'OUT1\n')   # Turn on if not already
    for i in range(10000):
        sdev.write(b'VSET1:30.1\n')
        sdev.write(b'VSET1?\n')
        print('{:%Y/%m/%d %H:%M:%S}, Count: {}, Set: {} volts for {:.1f} minutes'.format(datetime.datetime.now(), i, sdev.readline().decode('utf-8').strip(), time_at_30v_s/60.0))
        time.sleep(time_at_30v_s)
        sdev.write(b'VSET1:24.1\n')
        sdev.write(b'VSET1?\n')
        print('{:%Y/%m/%d %H:%M:%S}, Count: {}, Set: {} volts for {:.1f} minutes'.format(datetime.datetime.now(), i, sdev.readline().decode('utf-8').strip(), time_at_24v_s/60.0))
        time.sleep(time_at_24v_s)

from machine import Pin
import time
led = Pin(2, Pin.OUT)

time.sleep(1)
led.value(1)
time.sleep(1)
led.value(0)
time.sleep(1)
led.value(1)
time.sleep(1)
led.value(0)
time.sleep(1)
led.value(1)
time.sleep(1)
led.value(0)
time.sleep(1)
led.value(1)
time.sleep(1)
led.value(0)

button = Pin(0, Pin.IN)


if button() == 0:
    print('boot button pressed')
    ugit.pull_all()
    print('pulling github repo')

    

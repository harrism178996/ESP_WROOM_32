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


#if button() == 0:
#   print('boot button pressed')
#    ugit.pull_all()
#    print('pulling github repo')
    

button = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_UP)
while True:
    first = button.value()
    time.sleep(0.01)
    second = button.value()
    if first and not second:
        print('Button pressed!')
    elif not first and second:
        print('Button released!')
    

#!/usr/bin/env python3
#Code by Colin Twigg, Recognition Designs Ltd, 2021.

import sys
import time
try:
    import RPi.GPIO as GPIO
except ImportError:
    sys.exit("Cannot import RPi: Do `sudo apt-get install python3-dev python3-rpi.gpio` to in>

GPIO.setmode(GPIO.BCM)

PIR_PIN = 7
LED = 23
FAN = 25

GPIO.setup(LED,GPIO.OUT)
GPIO.setup(PIR_PIN, GPIO.IN)
GPIO.setup(FAN,GPIO.OUT)

try:
#    print('PIR Module Test (CTRL+C to exit)')
    time.sleep(1)
#    print('Ready')

    while True:
        if GPIO.input(PIR_PIN):
            time.sleep(2)
            GPIO.output(LED,GPIO.HIGH)
            GPIO.output(FAN,GPIO.LOW)
            time.sleep(2)
        else:
#           print('Motion Detected!')
            time.sleep(2)
#           print("switch off LED, turn on fan")
            GPIO.output(LED,GPIO.LOW)
            GPIO.output(FAN,GPIO.HIGH)

except KeyboardInterrupt:
#               print('Quit')
               GPIO.cleanup()
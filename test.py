import RPi.GPIO as GPIO
import time

pin = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    print GPIO.input(pin)
    time.sleep(.1)
GPIO.cleanup()

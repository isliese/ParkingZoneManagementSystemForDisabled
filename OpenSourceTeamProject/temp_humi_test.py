import RPi.GPIO as GPIO
import signal
import sys
import time

def signal_handler(signal, frame) :
    print('process stop')
    GPIO.cleanup()
    sys.exit()

signal.signal(signal.SIGINT, signal_handler)

GPIO.setmode(GPIO.BCM)

DHTPIN = 7

PULSES_CNT = 41
MAX_CNT = 320

def sizecvt(read) :
    if (read > 255 or read < 0):
        print("Invalid data from wiringPi library")
        sys.exit(1)
    return read

def read_dht22_dat():
    laststate = True
    count = 0
    MAX_CNT = 320
    j=0
    i=0

    GPIO.setup(DHTPIN, GPIO.OUT)
    GPIO.output(DHTPIN, True)
    time.sleep(0.01)

    GPIO.output(DHTPIN, False)
    time.sleep(0.018)

    GPIO.setup(DHTPIN, GPIO.IN)

    for i in range(10):
        pass

while True:
    read_dht22_dat()

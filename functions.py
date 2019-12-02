# - motion_detect():
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)


def motion_detect():
    """Check if the PIR sensor attached at BOARD port 11 is detecting motion and returns True or False
    """
    return GPIO.input(11)
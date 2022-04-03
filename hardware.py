import time
import grovepi

def _input(pin):
    try:
        grovepi.pinMode(pin,"INPUT")
        return grovepi.analogRead(pin)
    except IOError:
        return "N/O"

def _output(pin,swit):
    if pin not in [2,3,4,5,6,7,8] or swit not in [0,1]: return "N/O"
    try:
        grovepi.pinMode(pin,"OUTPUT")
        return grovepi.digitalWrite(pin,swit)
    except IOError:
        return "N/O"

def _input_ag(pin):
    try:
        grovepi.pinMode(pin,"INPUT")
        return grovepi.analogRead(pin)
    except IOError:
        return "N/O"

def _dig_input(pin):
    try:
        grovepi.pinMode(pin,"INPUT")
        return grovepi.digitalRead(pin)
    except IOError:
        return "N/O"

def _read_ultra(pin):
    return grovepi.ultrasonicRead(pin)

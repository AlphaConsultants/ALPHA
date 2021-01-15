import time
import RPi.GPIO as GPIO
GPIO.setmode( GPIO.BCM )
GPIO.setwarnings( 0 )

print( "GPIO pulse" )


def pulse(led, delay1, delay2):
    """
    Geef een puls op de pin:
    Maak de pin pin_nr hoog, wacht high_time,
    maak de pin laag, en wacht nog low_time
    """
    # copieer hier je implementatie van pulse
    GPIO.output(led, GPIO.HIGH)
    time.sleep(delay1)
    GPIO.output(led, GPIO.LOW)
    time.sleep(delay2)

GPIO.setup(18, GPIO.OUT)


def servo_pulse(pin_nr, position):
    """
    Send a servo pulse on the specified gpio pin
    that causes the servo to turn to the specified position, and
    then waits 20 ms.

    The position must be in the range 0 .. 100.
    For this range, the pulse must be in the range 0.5 ms .. 2.5 ms

    Before this function is called,
    the gpio pin must be configured as output.
    """

    # implementeer deze functie
    pulse(pin_nr, 0.0005 + (0.00002 * position), 0.02)


GPIO.setup(23, GPIO.OUT)

GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def switch_leuk_feitje(output):
    while True:
        if(GPIO.input(24)):
            output
            return False


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

GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


def switch_on(output):
    while True:
        if(GPIO.input(24)):
            output
            return False



GPIO.setup(21, GPIO.OUT)
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def sr04(trig_pin, echo_pin):
    """
    Return the distance in cm as measured by an SR04
    that is connected to the trig_pin and the echo_pin.
    These pins must have been configured as output and input.s
    """

    # send trigger pulse
    # inplement this step
    GPIO.output(trig_pin, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(trig_pin, GPIO.LOW)

    start_tijd = time.time()

    while GPIO.input(echo_pin) == 0:
        start_tijd = time.time()

    stop_tijd = time.time()

    while GPIO.input(echo_pin) == 1:
        stop_tijd = time.time()

    # calculate and return distance
    # inplement this step
    duratie = stop_tijd - start_tijd

    #
    afstand = (34300 * duratie) // 2

    return afstand

def afstandssensor_koppeling():
    while True:
        sr04(21, 20)
        if sr04(21, 20) <= 5:
            print("koppeling is ingedrukt")
            return False


PIN_DATA  = 13
PIN_LATCH = 6
PIN_CLOCK = 5
GPIO.setup(PIN_DATA,  GPIO.OUT)
GPIO.setup(PIN_LATCH, GPIO.OUT)
GPIO.setup(PIN_CLOCK, GPIO.OUT)

def shiftout(byte):
  GPIO.output(PIN_LATCH, 0)
  for x in range(8):
    GPIO.output(PIN_DATA, (byte >> x) & 1)
    GPIO.output(PIN_CLOCK, 1)
    GPIO.output(PIN_CLOCK, 0)
  GPIO.output(PIN_LATCH, 1)

def lightshow():
    for x in range(255):
      shiftout(x)
      time.sleep(0.02)
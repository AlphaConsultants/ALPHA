import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(0)

print("GPIO pulse")


def pulse(led, delay1, delay2):
    """
    Geef een puls op de pin:
    Maak de pin pin_nr hoog, wacht high_time,
    maak de pin laag, en wacht nog low_time
    """
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
    pulse(pin_nr, 0.0005 + (0.00002 * position), 0.02)


GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


def switch_on(output):
    while True:
        if (GPIO.input(24)):
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


DATA = 13
LATCH = 6
CLOCK = 5
GPIO.setup(DATA, GPIO.OUT)
GPIO.setup(LATCH, GPIO.OUT)
GPIO.setup(CLOCK, GPIO.OUT)


def schuif_register(byte):
    GPIO.output(LATCH, 0)
    for x in range(8):
        GPIO.output(DATA, (byte >> x) & 1)
        GPIO.output(CLOCK, 1)
        GPIO.output(CLOCK, 0)
    GPIO.output(LATCH, 1)


def lightshow():
    for x in range(255):
        schuif_register(x)
        time.sleep(0.02)


print("neopixels walk")

clock_pin = 19
data_pin = 26

GPIO.setup(clock_pin, GPIO.OUT)
GPIO.setup(data_pin, GPIO.OUT)


def apa102_send_bytes(clock_pin, data_pin, bytes):
    """
    zend de bytes naar de APA102 LED strip die is aangesloten op de clock_pin en data_pin
    """

    # implementeer deze functie:
    for byte in bytes:
        for bit in byte:
            if bit == 1:
                GPIO.output(data_pin, GPIO.HIGH)
            else:
                GPIO.output(data_pin, GPIO.LOW)
            GPIO.output(clock_pin, GPIO.HIGH)
            GPIO.output(clock_pin, GPIO.LOW)


def apa102_aan(clock_pin, data_pin, colors):
    """
    zend de colors naar de APA102 LED strip die is aangesloten op de clock_pin en data_pin

    De colors moet een list zijn, met ieder list element een list van 3 integers,
    in de volgorde [ blauw, groen, rood ].
    Iedere kleur moet in de range 0..255 zijn, 0 voor uit, 255 voor vol aan.

    bv: colors = [ [ 0, 0, 0 ], [ 255, 255, 255 ], [ 128, 0, 0 ] ]
    zet de eerste LED uit, de tweede vol aan (wit) en de derde op blauw, halve sterkte.
    """

    # implementeer deze functie, maak gebruik van de apa102_send_bytes functie
    apa102_send_bytes(clock_pin, data_pin, [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
    for i in range(8):
        apa102_send_bytes(clock_pin, data_pin, [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])
    # apa102_send_bytes(clock_pin, data_pin, [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
    for i in range(8):
        apa102_send_bytes(clock_pin, data_pin, [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])


blue = [8, 0, 0]
green = [0, 255, 0]
red = [0, 0, 255]


def colors(x, n, on, off):
    result = []
    for i in range(0, n):
        if i == x:
            result.append(on)
        else:
            result.append(off)
    return result


def walk(clock_pin, data_pin, delay, n=8):
    while True:
        for x in range(0, n):
            apa102_aan(clock_pin, data_pin, colors(x, n, red, blue))
            time.sleep(delay)
        # for x in range(n - 2, 0, -1):
        #     apa102_aan(clock_pin, data_pin, colors(x, n, red, blue))
        #     time.sleep(delay)

        return False

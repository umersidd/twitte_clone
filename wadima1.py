import RPi.GPIO as GPIO
import time
import Adafruit_DHT

# pins
onLedPin = 14
emLedPin = 23
buzzerPin = 27
servoPin = 26
startPushButtonPIn = 27
resetButton = 22
dht11Pin = 21
temperatureSensor = Adafruit_DHT.DHT11

# Pins Assigning
GPIO.setmode(GPIO.BCM)
GPIO.setup(onLedPin, GPIO.OUT)
GPIO.setup(emLedPin, GPIO.OUT)
GPIO.setup(buzzerPin, GPIO.OUT)
GPIO.setup(servoPin, GPIO.OUT)
GPIO.setup(startPushButtonPIn, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(resetButton, GPIO.IN, pull_up_down=GPIO.PUD_UP)

servo = GPIO.PWM(servoPin, 50)
servo.start(0)

def startFunction():
    temperature = Adafruit_DHT.read_retry(temperatureSensor, dht11Pin)
    print('Temperature: {0:0.1f}°C'.format(temperature))
    GPIO.output(onLedPin, GPIO.HIGH)

    if 30 < temperature <= 40:
        servo.ChangeDutyCycle(7.5)
        GPIO.output(onLedPin, GPIO.LOW)
        servo.ChangeDutyCycle(2.5)  # move servo to 0

    elif temperature > 40:
        GPIO.output(emLedPin, GPIO.HIGH)
        GPIO.output(buzzerPin, GPIO.HIGH)
        servo.ChangeDutyCycle(12.5)  # move servo to 180

        while GPIO.input(resetButton) == GPIO.HIGH:
            time.sleep(0.1)

            
            GPIO.output(emLedPin, GPIO.LOW)
            GPIO.output(buzzerPin, GPIO.LOW)
            servo.ChangeDutyCycle(2.5)  # move servo to 0

def resetFunction():
    GPIO.output(onLedPin, GPIO.LOW)
    GPIO.output(emLedPin, GPIO.LOW)
    GPIO.output(buzzerPin, GPIO.LOW)
    servo.ChangeDutyCycle(2.5)  # move servo to 0

try:
    while True:
        if GPIO.input(startPushButtonPIn) == GPIO.LOW:
            startFunction()

        if GPIO.input(resetButton) == GPIO.LOW:
            resetFunction()

except KeyboardInterrupt:
    servo.stop()
    GPIO.cleanup()

from tkgpio import TkCircuit
configuration = {
 "width": 200,
 "height": 200,
 "leds": [{"x": 50, "y": 75, "name": "OnLed", "pin": 14},
 {"x": 75, "y": 75, "name": "EMLed", "pin": 23}],
 "servos": [
 {"x": 60, "y": 75, "name": "Servo", "pin": 26, "min_angle": -90, "max_angle": 90, 
"initial_angle": 0}],
 "buttons": [{"x": 60, "y": 75, "name": "StartPb", "pin": 27},
 {"x": 60, "y": 75, "name": "ResetPb", "pin": 22}],
 "temp_sensors": [{"x": 75, "y": 75, "name": "tempVal", "channel": 2}],
 "Buzzers": [{"x": 50, "y": 75, "name": "Buzzer", "pin": 0}
 ]
}
circuit = TkCircuit(configuration)
@circuit.run

def main():
    from gpiozero import LED, Button, Servo 
    import time
    import Adafruit_DHT

    # Pins
    onLedPin = LED(14)
    emLedPin = LED(23)
    buzzerPin = LED(0)
    servoPin = Servo(26)
    startPushButton = Button(27, pull_up=True)
    resetButton = Button(22, pull_up=True)
    dht11Pin = 21
    tempVal = Adafruit_DHT.DHT11

    def tempReading():
        tempValue = Adafruit_DHT.read_retry(tempVal, dht11Pin)
        print('tempValue: {0:0.1f}°C'.format(tempValue))

        onLedPin.on()

        if 30 < tempValue <= 40:
            servoPin.value = 0.0
            onLedPin.off()
            servoPin.value = -1.0  # move servo to 0

        elif tempValue > 40:
            emLedPin.on()
            buzzerPin.on()
            servoPin.value = 1.0  # move servo to 180

            resetButton.wait_for_release()

            emLedPin.off()
            buzzerPin.off()
            servoPin.value = -1.0  # move servo to 0

    def resetFunction():
        onLedPin.off()
        emLedPin.off()
        buzzerPin.off()
        servoPin.value = -1.0  # move servo to 0

    try:
        while True:
            if startPushButton.is_pressed:
                tempReading()

            if resetButton.is_pressed:
                resetFunction()

    except KeyboardInterrupt:
        pass
    finally:
        servoPin.close()
        onLedPin.close()
        emLedPin.close()
        buzzerPin.close()

if __name__ == "__main__":
    main()

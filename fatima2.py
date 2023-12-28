from tkgpio import TkCircuit
configuration = {
 "width": 200,
 "height": 200,
 "leds": [{"x": 50, "y": 75, "name": "OnLed", "pin": 3},
 {"x": 75, "y": 75, "name": "EMLed", "pin": 14}],
 "servos": [
 {"x": 60, "y": 75, "name": "Servo", "pin": 25, "min_angle": -90, "max_angle": 90, 
"initial_angle": 0}],
 "buttons": [{"x": 60, "y": 75, "name": "StartPb", "pin": 17},
 {"x": 60, "y": 75, "name": "ResetPb", "pin": 27}],
 "temp_sensors": [{"x": 75, "y": 75, "name": "TempSensor", "channel": 2}],
 "Buzzers": [{"x": 50, "y": 75, "name": "Buzzer", "pin": 16}
 ]
}
circuit = TkCircuit(configuration)
@circuit.run

def main():
    from gpiozero import LED, Button, Servo
    import time
    import Adafruit_DHT

    # Pins
    onLedState = LED(3)
    emLedState = LED(14)
    buzzerState = LED(16)
    servoMotor = Servo(25)
    startPushButton = Button(17, pull_up=True)
    resetButton = Button(27, pull_up=True)
    tempPin = 21
    temperatureSensor = Adafruit_DHT.DHT11

    # Define states
    class States:
        S0, S1, S2 = range(3)

    current_state = States.S0

    def startFunction():
        nonlocal current_state
        # Read temperature from the sensor
        temperature = Adafruit_DHT.read_retry(temperatureSensor, tempPin)
        print('Temperature: {0:0.1f}°C'.format(temperature))

        # Turn on the indicator LED
        onLedState.on()

        # State transition based on temperature
        switch_temperature = {
            30 < temperature <= 40: States.S1,
            temperature > 40: States.S2
        }

        current_state = switch_temperature.get(True, States.S0)

    def resetFunction():
        nonlocal current_state
        # Turn off all indicators and reset servo position
        onLedState.off()
        emLedState.off()
        buzzerState.off()
        servoMotor.value = -1.0  # move servo to 0

        # State transition to initial state
        current_state = States.S0

    try:
        while True:
            # State machine
            if current_state == States.S0:
                # Handle state S0
                pass

            elif current_state == States.S1:
                # Handle state S1
                startFunction()

            elif current_state == States.S2:
                # Handle state S2
                emLedState.on()
                buzzerState.on()
                servoMotor.value = 1.0  # move servo to 180

                resetButton.wait_for_release()

                emLedState.off()
                buzzerState.off()
                servoMotor.value = -1.0  # move servo to 0

                # State transition to initial state
                current_state = States.S0

    except KeyboardInterrupt:
        pass
    finally:
        # Clean up GPIO resources
        servoMotor.close()
        onLedState.close()
        emLedState.close()
        buzzerState.close()

if __name__ == "__main__":
    main()

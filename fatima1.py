from tkgpio import TkCircuit
configuration = {
 "width": 200,
 "height": 200,
 "leds": [{"x": 50, "y": 40, "name": "led1", "pin": 17},
 {"x": 50, "y": 40, "name": "led2", "pin": 3}, {"x": 50, "y": 40, "name": "led3", 
"pin": 14}],
 "motors": [{"x": 50, "y": 40, "name": "DC Motor", "clockWise_pin": 24}],
 "servos": [
 {"x": 50, "y": 40, "name": "Servo Motor", "pin": 25, "min_angle": -90, "max_angle": 
90, "initial_angle": 0}],
 "buttons": [{"x": 50, "y": 40, "name": "startButton", "pin": 7},
 {"x": 50, "y": 40, "name": "arrowButton", "pin": 12}]
}

circuit = TkCircuit(configuration)
@circuit.run

def main():
    # importing libraries
    import time
    import tkinter as tk
    from gpiozero import LED, Button, dcMotor, AngularServo
    import cv2

    current_state, start_time = "S0"

    # Pins 
    motor_1 = dcMotor(clockWise=24, backward=None)  # Replace None with the backward pin if available
    servo_motor = AngularServo(25)
    ledOne, ledTwo, ledThree = LED(17), LED(3), LED(14)
    arrow_button, start_PB = Button(7), Button(12)

    # Load the Haarcascades classifier for face detection process
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Function to detect faceSaved in an image
    def facial_detection(face_images):
        gray = cv2.cvtColor(face_images, cv2.COLOR_BGR2GRAY)
        faceSaved = face_cascade.detectMultiScale(gray, scaleFactor=2.9, minNeighbors=5)
        return len(faceSaved) > 0

    # Functions
    def change_state(next_state):
        nonlocal current_state, start_time
        current_state, start_time = next_state, time.time()

    # Function to update the state machine
    if start_PB.is_pressed:
        while True:
            if current_state == "S0":
                motor_1.clockWise(0)
                ledOne.off()
                ledTwo.off()
                ledThree.off()

            elif current_state == "S1":
                motor_1.clockWise(0.5)
                ledOne.on()
                ledTwo.off()
                ledThree.off()

                # S1 stay
                if time.time() - start_time > 5:
                    change_state("S2")

            elif current_state == "S2":
                servo_motor.angle = 0
                ledOne.off()
                ledTwo.on()
                ledThree.off()

            elif current_state == "S3":
                cap = cv2.VideoCapture(0)
                ret, frame = cap.read()

                # Perform face detection
                face_detected = facial_detection(frame)
                if face_detect():
                    ledOne.off()
                    ledTwo.off()
                    ledThree.on()

            # Checking buttons
            if arrow_button.is_pressed and current_state == "S3":
                current_state = "S0"
                   

            time.sleep(0.01)

    # Cleanup process
    motor_1.stop()
    servo_motor.detach()
    ledOne.off()
    ledTwo.off()
    ledThree.off()

if __name__ == "__main__":
    main()

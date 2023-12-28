from tkgpio import TkCircuit
#Khaled Al Nuaimi 1079530
configuration = {
 "width": 200,
 "height": 200,
 "leds": [{"x": 50, "y": 40, "name": "led1", "pin": 2},
 {"x": 50, "y": 40, "name": "led2", "pin": 3}, {"x": 50, "y": 40, "name": "led3", 
"pin": 4}],
 "motors": [{"x": 50, "y": 40, "name": "DC Motor", "forward_pin": 24, "backward_pin": 
25}],
 "servos": [
 {"x": 50, "y": 40, "name": "Servo Motor", "pin": 23, "min_angle": -90, "max_angle": 
90, "initial_angle": 0}],
 "buttons": [{"x": 50, "y": 40, "name": "startPb", "pin": 13},
 {"x": 50, "y": 40, "name": "secondPb", "pin": 19}]
}
circuit = TkCircuit(configuration)
@circuit.run
def main():
 from gpiozero import LED, Button, Motor, AngularServo
 from os import system
 from threading import Timer
 from imutils.video import VideoStream
 import cv2
 import pkg_resources
 from pynput.keyboard import Listener
 from pynput import keyboard
 onEntryS0, onstayS0, onEntryS1, onstayS1, onEntryS2, onstayS2, onEntryS3, onstayS3 = 
range(8)
 current = onEntryS0
 haar_file = pkg_resources.resource_filename('cv2', 
'data/haarcascade_frontalface_default.xml')
 face_cascade = cv2.CascadeClassifier(haar_file)
 vs = VideoStream(src=0).start()
 startPb = Button(13)
 secondPb = Button(19)
 led1 = LED(2)
 led2 = LED(3)
 led3 = LED(4)
 DCMotor = Motor(24, 25)
 ServoMotor = AngularServo(23)
 def startButtonPressed():
 nonlocal current
 if current == onstayS0:
 current = onEntryS1
 def delay5seconds():
 global current
 if current == onstayS1:
 current = onEntryS2
 def secondButtonPressed():
 nonlocal current
 if current == onstayS2:
 current = onEntryS3
 def on_press(key):
 global current
 print()
 print('{0} key is pressed'.format(key))
 if key == keyboard.Key.right and current == onstayS3:
 current = onEntryS0
 Listener(on_press =on_press).start()
 startPb.when_pressed = startButtonPressed
 secondPb.when_pressed = secondButtonPressed
 while True:
 if current == onEntryS0:
 current = onstayS0
 elif current == onstayS0:
 DCMotor.forward(0)
 ServoMotor.angle = int(0)
 led1.off()
 led2.off()
 led3.off()
 elif current == onEntryS1:
 current = onstayS1
 Timer(5.0, delay5seconds).start()
 elif current == onstayS1:
 DCMotor.forward(0.5)
 ServoMotor.angle = int(0)
 led1.on()
 led2.off()
 led3.off()
 elif current == onEntryS2:
 current = onstayS2
 elif current == onstayS2:
 DCMotor.forward(0)
 ServoMotor.angle = int(90)
 led1.off()
 led2.on()
 led3.off()
 elif current == onEntryS3:
 current = onstayS3
 elif current == onstayS3:
 img = vs.read()
 faces = face_cascade.detectMultiScale(img, 1.4, 5)
 print(faces)
 if len(faces) > 0:
 print("Detected faces")
 DCMotor.forward(0)
ServoMotor.angle = int(0)
 led1.off()
led2.off()
led3.on()
 else:
 print("faces were not detected, please try again!"

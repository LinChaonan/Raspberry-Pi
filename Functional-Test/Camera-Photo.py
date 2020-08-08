from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
sleep(5)
camera.capture('/home/pi/Desktop/Raspberry-Pi/Functional-Test/image.jpg' )
camera.stop_preview()
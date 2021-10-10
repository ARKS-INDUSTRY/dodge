#usr etc/bin/python
import RPi.GPIO as GPIO
import keyboard as key
import time


servo_black = 13
servo_blue = 19
right_forward = 22
right_backward = 27
left_forward = 24
left_backward = 23

GPIO.setup(servo_black, GPIO.OUT)
GPIO.setup(servo_blue, GPIO.OUT)

pwm_black=GPIO.PWM(servo_black, 50)
pwm_black.start(0)
pwm_blue=GPIO.PWM(servo_blue, 50)
pwm_blue.start(0)

def initialise():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(right_forward, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(right_backward, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(left_forward, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(left_backward, GPIO.OUT, initial=GPIO.LOW)
    

def forward():
    initialise()
    GPIO.output(right_forward, GPIO.HIGH)
    GPIO.output(left_forward, GPIO.HIGH)

def backward():
    initialise()
    GPIO.output(right_backward, GPIO.HIGH)
    GPIO.output(left_backward, GPIO.HIGH)

def right():
    initialise()
    GPIO.output(right_backward, GPIO.HIGH)
    GPIO.output(left_forward, GPIO.HIGH)

def left():
    initialise()
    GPIO.output(right_forward, GPIO.HIGH)
    GPIO.output(left_backward, GPIO.HIGH)
    
def stop():
    GPIO.cleanup()
    quit()

def servo_360(angle):
    pwm_black.ChangeDutyCycle(5) # left -90 deg position
    time.sleep(1)
    pwm_black.ChangeDutyCycle(7.5) # neutral position
    time.sleep(1)
    pwm_black.ChangeDutyCycle(10) # right +90 deg position
    time.sleep(1)
    
def servo_180(angle):
    pwm_blue.ChangeDutyCycle(5) # left -90 deg position
    time.sleep(1)
    pwm_blue.ChangeDutyCycle(7.5) # neutral position
    time.sleep(1)
    pwm_blue.ChangeDutyCycle(10) # right +90 deg position
    time.sleep(1)

def arm(angle1, angle2):
    time(0.5)
    print("servo")
    
def main():
    initialise()
    while True:
        if key.is_pressed('w') or key.is_pressed('up'):
            print('forward')
            forward()
            time.sleep(0.1)
            GPIO.cleanup()
            if key.is_pressed('s') or key.is_pressed('down'):
                print('backward')
            backward()
            time.sleep(0.1)
            GPIO.cleanup()
        if key.is_pressed('a') or key.is_pressed('left'):
            print('left')
            left()
            time.sleep(0.1)
            GPIO.cleanup()
        if key.is_pressed('d') or key.is_pressed('right'):
            print('right')
            right()
            time.sleep(0.1)
            GPIO.cleanup()
        if key.is_pressed('q'):
            print('servo')
            arm()
            time.sleep(0.1)
        if key.is_pressed(' '):
            print('stop')
            stop()
main()

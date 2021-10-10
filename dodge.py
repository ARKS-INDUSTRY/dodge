#https://sourceforge.net/p/raspberry-gpio-python/wiki/PWM/
import RPi.GPIO as GPIO
import time

#adjust this to make the rover move straight 


pwm = 10
cdc = 15

right_forward = 22
right_backward = 27
left_forward = 24
left_backward = 23
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
pwm1=GPIO.PWM(right_backward, 50)
pwm2=GPIO.PWM(right_forward, 50)


def initialise():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(right_forward, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(right_backward, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(left_forward, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(left_backward, GPIO.OUT, initial=GPIO.LOW)
    
def forward():
    print("forward")
    GPIO.output(right_forward,GPIO.HIGH)
    pwm1.start(pwm)
    GPIO.output(left_forward,GPIO.HIGH)
    pwm2.start(pwm)

def backward():
    initialise()
    print('Backward')
    GPIO.output(right_backward,GPIO.HIGH)
    pwm1.start(pwm)
    GPIO.output(left_backward,GPIO.HIGH)
    pwm2.start(pwm)

def right():
    initialise()
    print('Right')
    GPIO.output(right_forward,GPIO.HIGH)
    pwm1.start(pwm)
    time.sleep(0.1)
    pwm1.ChangeDutyCycle(cdc)
    GPIO.output(left_backward,GPIO.HIGH)
    pwm2.start(pwm)
    time.sleep(0.1)
    pwm2.ChangeDutyCycle(cdc)

def left():
    initialise()
    print('Left')
    GPIO.output(right_backward, GPIO.HIGH)
    pwm1.start(pwm)
    time.sleep(0.1)
    pwm1.ChangeDutyCycle(cdc)
    GPIO.output(left_forward, GPIO.HIGH)
    pwm2.start(pwm)
    time.sleep(0.1)
    pwm2.ChangeDutyCycle(cdc)
    
def stop():
    pwm1.stop()
    pwm2.stop()
    GPIO.cleanup()

def run():
    initialise()
    forward()
    time.sleep(3)
    GPIO.cleanup()

    initialise()
    backward()
    time.sleep(2)
    GPIO.cleanup()

    initialise()
    right()
    time.sleep(3)
    GPIO.cleanup()

    initialise()
    left()
    time.sleep(3)
    GPIO.cleanup()

    initialise()
    stop()
    time.sleep(2)
    GPIO.cleanup()

    initialise()
    forward()
    time.sleep(5)
    GPIO.cleanup()

    initialise()
    backward()
    time.sleep(5)
    GPIO.cleanup()
    
    initialise()
    stop()

run()



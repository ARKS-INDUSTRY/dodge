import RPi.GPIO as GPIO
import time

right_forward = 22
right_backward = 27
left_forward = 24
left_backward = 23
servo = 4
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(servo, GPIO.OUT)
pwm=GPIO.PWM(servo, 50)
pwm.start(0)

def servo(angle):
    duty = angle / 18 + 2
    pwm.ChangeDutyCycle(duty)
    time.sleep(2)
    pwm.stop(0)

servo(0)

def initialise():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(right_forward, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(right_backward, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(left_forward, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(left_backward, GPIO.OUT, initial=GPIO.LOW)
    
    

def forward():
    initialise()
    print('Forward')
    GPIO.output(right_forward, GPIO.HIGH)
    GPIO.output(left_forward, GPIO.HIGH)

def backward():
    initialise()
    print('Backward')
    GPIO.output(right_backward, GPIO.HIGH)
    GPIO.output(left_backward, GPIO.HIGH)

def right():
    initialise()
    print('Right')
    GPIO.output(right_backward, GPIO.HIGH)
    GPIO.output(left_forward, GPIO.HIGH)

def left():
    initialise()
    print('Left')
    GPIO.output(right_forward, GPIO.HIGH)
    GPIO.output(left_backward, GPIO.HIGH)
    
def stop():
    GPIO.cleanup()
    quit()



def arm():
    servo(60)
    time.sleep(1)
    servo(0)
    time.sleep(0.5)

def main():
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
    arm()
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

main()

#arudhran when u r codding compile
import RPi.GPIO as GPIO
import time
import random

pins = [11, 12, 13]

def setup():
    global pwmRed, pwmGreen, pwmBlue
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pins, GPIO.OUT)
    GPIO.output(pins, GPIO.HIGH)
    pwmRed = GPIO.PWM(pins[0], 2000) # Set frequency to 2kHz
    pwmGreen = GPIO.PWM(pins[1], 2000) # Set frequency to 2kHz
    pwmBlue = GPIO.PWM(pins[2], 2000) #Set frequency to 2kHz
    pwmRed.start(0)
    pwmGreen.start(0)
    pwmBlue.start(0)

def setColor(r,g,b):
    pwmRed.ChangeDutyCycle(r)
    pwmGreen.ChangeDutyCycle(g)
    pwmBlue.ChangeDutyCycle(b)

def loop():
    while True:
       # r=random.randint(0,100)
       # g=random.randint(0,100)
       # b=random.randint(0,100)
       # setColor(r,g,b)
       # print('r=%d, g=%d, b=%d '%(r,g,b))
       # time.sleep(1)

      for r in range(100):
          for g in range(100):
              for b in range(100):
                  setColor(r,g,b)
                  time.sleep(.1)


def destroy():
    pwmRed.stop()
    pwmGreen.stop()
    pwmBlue.stop()
    GPIO.cleanup()

if __name__ == '__main__':
    print("Program is starting...")
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()

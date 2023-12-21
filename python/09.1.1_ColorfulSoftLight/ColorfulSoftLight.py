import RPi.GPIO as GPIO
import time
from ADCDevice import *

ledRedPin = 13
ledGreenPin = 11
ledBluePin = 15
adc = ADCDevice()

def setup():
    global adc
    if(adc.detectI2C(0x4b)):
        adc=ADS7830()

    else:
        print("No correct I2C address found, \n"
                "please us command 'i2cdetect -y 1' to check the i2c address! \n"
                "Progam Exit. \n");
        exit(-1)

    global p_Red, p_Green, p_Blue
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ledRedPin, GPIO.OUT)
    GPIO.setup(ledGreenPin, GPIO.OUT)
    GPIO.setup(ledBluePin, GPIO.OUT)

    p_Red = GPIO.PWM(ledRedPin, 1000)
    p_Red.start(0)
    p_Green = GPIO.PWM(ledGreenPin, 1000)
    p_Green.start(0)
    p_Blue = GPIO.PWM(ledBluePin, 1000)
    p_Blue.start(0)

def loop():
    while True: 
        value_Red = adc.analogRead(0)
        value_Green = adc.analogRead(1)
        value_Blue = adc.analogRead(2)
        p_Red.ChangeDutyCycle(value_Red*100/255)
        p_Green.ChangeDutyCycle(value_Green*100/255)
        p_Blue.ChangeDutyCycle(value_Blue*100/255)
        print("ADC Value\nvalue_Red: %d , \tvalue_Green: %d , \tvalue_Blue : %d"%(value_Red,value_Green,value_Blue))
        time.sleep(0.01)

def destroy():
    adc.close()
    p_Red.stop()
    p_Green.stop()
    p_Blue.stop()
    GPIO.cleanup()

if "__main__" == __name__:
    print("Program is starting...")
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()

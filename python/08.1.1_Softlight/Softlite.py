import RPi.GPIO as GPIO
import time
from ADCDevice import *

ledPin = 11
adc = ADCDevice()

def setup():
    global adc
    if(adc.detectI2C(0x4b)):
        adc = ADS7830()
    else: 
        print("No correct I2C address found, \n"
                "Please use command 'i2cdetect -y 1' to check the I2C address! \n"
                "Program Exit. \n");

    global p
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ledPin, GPIO.OUT)
    p = GPIO.PWM(ledPin,1000)
    p.start(0)

def loop():
    while True:
        value = adc.analogRead(0)
        p.ChangeDutyCycle(value*100/255)
        voltage = value / 255.0 * 3.3
        print("ADC Value : %d, Voltage : %.2f"%(value,voltage))
        time.sleep(0.03)

def destroy():
    adc.close()

if "__main__" == __name__:
    print("Program starting...")
    try:
        setup()
        loop()
    except KeyboardInterrupt:
        destroy()
        

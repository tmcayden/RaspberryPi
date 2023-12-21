#Test code to ensure button functionality

from gpiozero import LED, Button
from signal import pause

print("Program is starting")

led = LED(17)
button = Button(18)

def onButtonPressed():
    led.on()
    print("Button is pressed, led turned on >>>")

def onButtonReleased():
    led.off()
    print("Button is released, led turned off <<<")

button.when_pressed = onButtonPressed
button.when_released = onButtonReleased

pause()

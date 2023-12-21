# Button as a switch for LED

from gpiozero import LED, Button
from signal import pause

print("Program is starting")

led = LED(17)
button = Button(18)

def onButtonPressed():
    led.toggle()
    if led.is_lit:
        print("Led turned on >>>")
    else:
        print("Led turned off <<<")

button.when_pressed = onButtonPressed

pause()

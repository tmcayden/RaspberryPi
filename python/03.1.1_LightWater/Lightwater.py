# Waterfall looking light display


from gpiozero import LEDBoard
from time import sleep
from signal import pause

print("Program is starting..")

ledPins = ["J8:11", "J8:12", "J8:13", "J8:15", "J8:16", "J8:18", "J8:22", "J8:3", "J8:5", "J8:24"]

leds = LEDBoard(*ledPins, active_high=False)

while True:
    for i in range(2):
        for index in range(0,len(ledPins),1):
            leds.on(index)
            sleep(0.1)
            leds.off(index)
        for index in range(len(ledPins)-1, -1, -1):
            leds.on(index)
            sleep(0.1)
            leds.off(index)
    
        for index in range(0,len(ledPins),1):
            leds.on(index)
            sleep(0.3)
        for index in range(len(ledPins)-1, -1, -1):
            leds.off(index)
            sleep(0.3)
        
        for index in range(len(ledPins)-1, -1, -1):
            leds.on(index)
            sleep(0.3)
        for index in range(len(ledPins)-1, -1, -1):
            leds.off(index)
            sleep(0.3)

        tail = -2
        for i in range(5):
            for index in range(0, len(ledPins), 1):
                leds.on(index)
                leds.off(tail)
                tail=index-2
                sleep(0.1)

        leds.off(tail)
        sleep(0.1)
        leds.off(tail+1)
        sleep(0.1)
        leds.off(tail+2)
        sleep(0.1)

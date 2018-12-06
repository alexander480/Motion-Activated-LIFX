#!/usr/bin/python2

import RPi.GPIO as GPIO
from lifxlan import LifxLAN, BLUE, CYAN, GREEN, ORANGE, PINK, PURPLE, RED, YELLOW
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(7, GPIO.IN)

lifx=LifxLAN(2)
lights=lifx.get_lights()

original_color = lights[0].get_color()
lifx.set_power_all_lights("on")

rainbow(lights[0], 5.0)

empty=True
count=0

sleep(1)

print "-----------------------------------------"
print "-------------- LIFX Motion --------------"
print "-----------------------------------------"

if GPIO.input(7):
    ## lights[0].set_power("on", 1000)
    ## lights[1].set_power("on", 1000)
    lifx.set_color_all_lights(original_color)
    lifx.set_power_all_lights("on", 1000)
    empty=False
else:
    ## lights[0].set_power("off", 5000)
    ## lights[1].set_power("off", 5000)
    lifx.set_power_all_lights("off", 5000)
    empty=True

try:
    while True:
        if GPIO.input(7):
            if empty:
                print "Turning Lights On"
                ## lights[0].set_power("on", 1000)
                ## lights[1].set_power("on", 1000)
                lifx.set_power_all_lights("on", 1000)
                empty=False
                count = 0
            print "[" + str(count) + "] On"
            sleep(1)
            count=count+1
        else:
            if not empty:
                print "Turning Lights Off"
                empty=True
                ## lights[0].set_power("off", 5000)
                ## lights[1].set_power("off", 5000)
                lifx.set_power_all_lights("off", 5000)

except KeyboardInterrupt:
    print "--------------------------------------"
    print "-------------- Goodbye ---------------"
    print "--------------------------------------"
    GPIO.cleanup()

def rainbow(bulb):
    colors = [RED, ORANGE, YELLOW, GREEN, CYAN, BLUE, PURPLE, PINK]
    for color in colors:
        bulb.set_color(color, 0)
        sleep(5)

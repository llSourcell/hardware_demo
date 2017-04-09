#!usr/bin/env python2

import time

from subprocess import call

# use gpio pin out 18 to send pwm pulses to the servo
PIN = 18

# pwm pulse time in ms -- 1500ms pulse doesn't move the servo
# from product page: https://www.adafruit.com/products/154
#   Position "90" (1.5ms pulse) is stop, "180" (2ms pulse) is full speed forward,
#   "0" (1ms pulse) is full speed backwards.
NEUTRAL = 1500
# +200 ms to the base pulse to turn the blinds down slowly
DOWN = 200
# -200 ms to the base pulse to turn the blinds up slowly
UP = -200

# time in seconds
SERVO_RUNTIME = 4

class Blinds:
    def __init__(self):
        self.opened = True # start with blinds at neutral
        self.closed = False
        self.moving = False

    def run_servo(self, direction):
        '''
        Used to encapsulate turning the servo.

        Right now performing hack to shell out to `pigs` command line tool which
        works exactly as expected. I don't know how to control the servo correctly
        yet with the python bindings of the pigpio library. Once I learn how to
        do that, I'll change the underlying implementation of this method
        '''
        call(["pigs", "s", "{}".format(PIN), "{}".format(direction)])
        
    def open(self):
        # set that we're no longer closed
        self.closed = False
        
        # currently already open or in the process of moving
        if self.opened or self.moving:
            return

        # debugging output
        print('open')

        # set that we're moving
        self.moving = True

        # send pwm signal to open the blinds
        self.run_servo(NEUTRAL + UP)

        # sleep to let the servo move
        time.sleep(SERVO_RUNTIME)

        # reset servo to neutral to stop moving
        self.run_servo(NEUTRAL)

        # set that we've finished moving
        self.moving = False

        # set that we're open
        self.opened = True
 
    def close(self):
        # set that we're no longer open
        self.opened = False

        # currently already closed or in the process of moving
        if self.closed or self.moving: 
            return

        # debugging output
        print('close')

        # set that we're moving
        self.moving = True
        
        # send pwm signal to close the blinds
        self.run_servo(NEUTRAL + DOWN)

        # sleep to let the servo move
        time.sleep(SERVO_RUNTIME)

        # reset servo to neutral to stop moving
        self.run_servo(NEUTRAL)

        # set that we've finished moving
        self.moving = False

        # set that we're closed
        self.closed = True
       

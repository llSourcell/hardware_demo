import time

from blinds import Blinds, NEUTRAL, UP, DOWN

# janky way to calibrate blinds to be open/closed to the right amount
# edit this file to change UP/DOWN to move blinds in desired direction,
# save and then run
def main():
    blinds = Blinds()
    blinds.run_servo(NEUTRAL + UP)
    time.sleep(1)
    blinds.run_servo(NEUTRAL)


if __name__ == '__main__':
   main()

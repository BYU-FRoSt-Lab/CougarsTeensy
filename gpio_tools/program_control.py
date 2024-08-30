##########################################################
# TURNS OFF AND ON THE CONTROL PROGRAM PIN
# - If control is on, a red light should light up on the
#   board after running this script
##########################################################

import time
import gpiod

from gpio_def import *

# open the gpio chip and set the control program pin as output
chip = gpiod.Chip('/dev/gpiochip4')
control_prog_line = chip.get_line(CONTROL_PROGRAM_PIN)
control_prog_line.request(consumer="CONTROL_PROG", type=gpiod.LINE_REQ_DIR_OUT)

print("Entering program mode on the Control Teensy . . .")

# set the GPIO pin low then high
control_prog_line.set_value(0)
time.sleep(2)
control_prog_line.set_value(1)

print(". . .")
time.sleep(5)

print("COMPLETE: Entered program mode on the Control Teensy")
control_prog_line.release()

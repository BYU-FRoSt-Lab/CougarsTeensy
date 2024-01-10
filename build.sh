#!/bin/bash

cd ~/teensy_ws/sensors
pio run

cd .pio/build/teensy41
teensy_loader_cli --mcu=TEENSY41 -sv firmware.hex
# teensy_loader_cli --mcu=TEENSY41 -sv firmware.hex
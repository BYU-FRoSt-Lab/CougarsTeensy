#!/bin/bash

cd ~/teensy_ws/control
pio run

cd .pio/build/teensy41
tycmd upload firmware.hex

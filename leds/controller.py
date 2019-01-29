#!/usr/bin/env python3

import time
import argparse
import animation as a

from color import Color
from neopixel import *

class Controller:
    def __init__(self):
        # LED strip configuration:
        self.LED_COUNT      = 270     # Number of LED pixels.
        self.LED_PIN_0      = 12      # GPIO pin connected to the pixels - CHANNEL 0
        self.LED_PIN_1      = 13      # GPIO pin connected to the pixels - CHANNEL 1

        self.LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
        self.LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
        self.LED_BRIGHTNESS = 100     # Set to 0 for darkest and 255 for brightest
        self.LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
        self.LED_CHANNEL_0  = 0       # set to '0' for GPIOs 12, 18
        self.LED_CHANNEL_1  = 1       # set to '1' for GPIOs 13, 19, 41, 45 or 53


    def setup(self):
        # Create NeoPixel object with appropriate configuration.
        self.strip0 = Adafruit_NeoPixel(LED_COUNT, 18, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, 0)
        self.strip1 = Adafruit_NeoPixel(LED_COUNT, 13, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, 1)
    
        # Intialize the library (must be called once before other functions).
        strip0.begin()
        strip1.begin()

#!/usr/bin/env python3

import time
import argparse
import animation as a

from neopixel import *
from threading import Thread

# LED strip configuration:
LED_COUNT      = 270    # Number of LED pixels.
LED_PIN_0      = 12      # GPIO pin connected to the pixels - CHANNEL 0
LED_PIN_1      = 13      # GPIO pin connected to the pixels - CHANNEL 1

LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 150     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL_0  = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
LED_CHANNEL_1  = 1

# Main program logic follows:
if __name__ == '__main__':
    # Process arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    args = parser.parse_args()

    # Create NeoPixel object with appropriate configuration.
    strip0 = Adafruit_NeoPixel(LED_COUNT, 18, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, 0)
    #strip1 = Adafruit_NeoPixel(LED_COUNT, 13, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, 1)
    
    # Intialize the library (must be called once before other functions).
    strip0.begin()
    #strip1.begin()

    print ('Press Ctrl-C to quit.')
    if not args.clear:
        print('Use "-c" argument to clear LEDs on exit')

    try:

        while True:
            #a.randomPixel(strip0)
            #a.bounce(strip0, Color(0,200,0),5)
            a.tetris(strip0)

    except KeyboardInterrupt:
        if args.clear:
            
            a.colorSet(strip0, Color(0,0,0))
            #a.colorWipe(strip1, Color(0,0,0), 10)

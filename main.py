#!/usr/bin/env python3

import sys
import time
import random
import argparse
import animation as a
import RPi.GPIO as GPIO
import numpy as np
import matplotlib.pyplot as plt

from neopixel import *
from threading import Thread
from gpiozero import MCP3008


# LED strip configuration:
LED_COUNT      = 270    # Number of LED pixels.
LED_PIN_0      = 12      # GPIO pin connected to the pixels - CHANNEL 0
LED_PIN_1      = 13      # GPIO pin connected to the pixels - CHANNEL 1

LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL_0  = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
LED_CHANNEL_1  = 1

# Spectrum board configuration:
STROBE = 3      # Pin 4 on Spectrum
RESET  = 4      # Pin 5 on Spectrum

# Spectrum frequency lists
FREQ = [i for i in range(7)]

# Initialize analog channels for Spectrum shield
data_0 = MCP3008(0)
data_1 = MCP3008(1) 
   
alive = True

# Setup GPIO pins
def setup_spectrum():
    # Set spectrum shield pin configs
    GPIO.setup(STROBE, GPIO.OUT)
    GPIO.setup(RESET, GPIO.OUT)
    
    GPIO.output(STROBE, GPIO.HIGH)
    GPIO.output(RESET, GPIO.HIGH)

    # Initialize spectrum analyzers
    GPIO.output(STROBE, GPIO.LOW)
    time.sleep(0.001)
    GPIO.output(RESET, GPIO.HIGH)
    time.sleep(0.001)
    GPIO.output(STROBE, GPIO.HIGH)
    time.sleep(0.001)
    GPIO.output(STROBE, GPIO.LOW)
    time.sleep(0.001)
    GPIO.output(RESET, GPIO.LOW)

def map(x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min)/(in_max - in_min) + out_min

def read_freq(threadname):
    global FREQ
    global data_0
    global data_1
    global alive

    try:
        while alive:
            for amp in range(7):
                if data_0.value > data_1.value:
                    FREQ[amp] = data_0.value
                else:
                    FREQ[amp] = data_1.value

                #FREQ[amp] = map(FREQ[amp], 0, 1, 0, 255) 
                FREQ[amp] *= 1000
                
                GPIO.output(STROBE, GPIO.HIGH)
                GPIO.output(STROBE, GPIO.LOW)
            else:
                pass
                #print FREQ
    except KeyboardInterrupt:
        alive = False  

# Main program logic follows:
if __name__ == '__main__':
    # Process arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    args = parser.parse_args()

    # Initialize analog channels for Spectrum shield
    #data_0 = MCP3008(0)
    #data_1 = MCP3008(1) 

    # Create NeoPixel object with appropriate configuration.
    strip0 = Adafruit_NeoPixel(LED_COUNT, 18, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, 0)
    strip1 = Adafruit_NeoPixel(LED_COUNT, 13, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, 1)
    
    # Intialize the library (must be called once before other functions).
    strip0.begin()
    strip1.begin()

    # Setup spectrum board control pins
    #setup_spectrum()

    # Start analog read thread
    #analog_thread = Thread(target=read_freq, args=("analog thread",))
    #analog_thread.start()

    print ('Press Ctrl-C to quit.')
    if not args.clear:
        print('Use "-c" argument to clear LEDs on exit')

    try:
        #a.colorSet(strip0, a.LIME)
        #a.colorSet(strip1, a.LIME)
        while alive:
            #a.colorWipe(strip0, a.WHITE)
            a.rainbowCycle(strip0, strip1)
            #a.theaterChaseRainbow(strip0, strip1, 125) 
            #a.theaterChaseRainbow(strip1)
            #a.randomPixel(strip0, a.CYAN)
            #a.bounce(strip0, Color(0,200,0))
            #a.tetris(strip0)
            #a.tetris(strip1)
            #color = strip0.getPixelColor(strip0.numPixels()/2)
            #color2= strip0.getPixelColor(1)
            #a.bounce_bar(strip0, color, color2)
            #a.bounce_bar(strip1, color, color2)
            
            #a.colorWipe(strip0, a.RED)
            #a.colorWipe(strip1, a.LIME, True)

            #a.colorWipe(strip0, a.LIME)
            #a.colorWipe(strip1, a.RED, True)

            #a.doubleWipe(strip0, strip1, a.MAGENTA, a.LIME)
            #a.police2(strip0, strip1)
            #a.xmas(strip0)
            #a.xmas(strip1)
            
            #strip0.show()
            #strip1.show()
            #time.sleep(16.67/1000.0)

            #a.colorWipe(strip0, a.WHITE)
            
            #print("[63Hz: {:>6.3f},\t160Hz: {:>6.3f},\t400Hz: {:>6.3f},\t1000Hz: {:>6.3f},\t2500Hz: {:>6.3f},\t6250Hz: {:>6.3f},\t16000Hz: {:>6.3f}]\r".format(FREQ[0], FREQ[1], FREQ[2], FREQ[3], FREQ[4], FREQ[5], FREQ[6])) 
            
            #for i in range(175):
            #    c0 = a.wheel(random.randint(0, 100))
            #    c1 = a.wheel(random.randint(101, 180))
            #    c2 = a.wheel(random.randint(181, 255))

            #    a.rotate_3(strip0,strip1,c0,c1,c2, True)
          
            #a.circular(strip0,strip1)
            #x = FREQ[0]
            #y = np.arange(0,1)
           
            
            #plt.plot(x, y)
            #plt.show()
            #pass

    except KeyboardInterrupt:
        alive = False
        if args.clear:
            a.colorSet(strip0, a.BLACK)
            a.colorSet(strip1, a.BLACK) 

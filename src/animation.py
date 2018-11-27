#!/usr/bin/env python3

import time
import random
from neopixel import *

#############################
# Colors  - G - R - B
#############################
BLACK   = Color(0,0,0)
WHITE   = Color(255,255,255)
RED     = Color(0,255,0)
LIME    = Color(255,0,0)
BLUE    = Color(0,0,255)
YELLOW  = Color(255,255,0)
CYAN    = Color(255,0,255)
MAGENTA = Color(0,255,255)
SILVER  = Color(192,192,192)
GRAY    = Color(128,128,128)
MAROON  = Color(0,128,0)
OLIVE   = Color(128,128,0)
GREEN   = Color(128,0,0)
PURPLE  = Color(0,128,128)
TEAL    = Color(128,0,128)
NAVY    = Color(0,0,128)
#############################

COLORS = [RED, LIME, BLUE, YELLOW, CYAN, MAGENTA]

def colorWipe(strip, color, invert = False, wait_ms = 2):
    """Wipe color across display a pixel at a time."""
    if invert == True:
        for i in reversed(range(strip.numPixels())):
            strip.setPixelColor(i, color)
            strip.show()
            time.sleep(wait_ms/1000.0)
    else:
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, color)
            strip.show()
            time.sleep(wait_ms/1000.0)

def colorSet(strip, color):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
    strip.show()

def theaterChase(strip, color, wait_ms=50, iterations=10):
    """Movie theater light style chaser animation."""
    for j in range(iterations):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, color)
            strip.show()
            time.sleep(wait_ms/1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, 0)

def wheel(pos):
    """Generate rainbow colors across 0-255 positions."""
    if pos < 85:
        return Color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return Color(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return Color(0, pos * 3, 255 - pos * 3)

def rainbow(strip, wait_ms=20, iterations=1):
    """Draw rainbow that fades across all pixels at once."""
    for j in range(256*iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((i+j) & 255))
        strip.show()
        time.sleep(wait_ms/1000.0)

def rainbowCycle(strip, wait_ms=50, iterations=50):
    """Draw rainbow that uniformly distributes itself across all pixels."""
    for j in range(256*iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((int(i * 256 / strip.numPixels()) + j) & 255))
        strip.show()
        time.sleep(wait_ms/1000.0)

def theaterChaseRainbow(strip, wait_ms=150):
    """Rainbow movie theater light style chaser animation."""
    for j in range(256):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, wheel((i+j) % 255))
            strip.show()
            time.sleep(wait_ms/1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, 0)

def pixel_chase(strip, wait_ms=1, tail=4):
    """Pixel races across with trail size"""
    for j in range(strip.numPixels()):
        k = 0
        for i in range(strip.numPixels()):
            if i == j:
                for t in range(tail):
                    strip.setPixelColor(i-t, wheel((int(j-t+k * 256 / strip.numPixels())+j) % 255))
            else:
                strip.setPixelColor(i, 0)

            k = k+1
        strip.show()
        time.sleep(wait_ms/1000.0)


def xmas(strip, wait_ms=500):
    flag = True

    for i in range(strip.numPixels()):
        if i % 5 == 0:
            flag = not flag
            if flag:
                strip.setPixelColor(i, Color(0,255,0))
            else:
                strip.setPixelColor(i, Color(255,0,0))
    strip.show()
    time.sleep(wait_ms/1000.0)
    for i in range(strip.numPixels()):
        if i % 5 == 0:
            flag = not flag
            if flag:
                strip.setPixelColor(i, Color(255,0,0))
            else:
                strip.setPixelColor(i, Color(0,255,0))
    strip.show()
    time.sleep(wait_ms/1000.0)


def risingColor(strip):
    for i in range(255):
        strip.setPixelColor(i, Color(i,0,i))
        strip.show()

def randomPixel(strip, wait_ms=500):
    strip.setPixelColor(random.randint(0, strip.numPixels()), GREEN)
    strip.show()
    time.sleep(wait_ms/1000.0)

def bounce(strip, color, wait_ms=50):
    for i in range(strip.numPixels()):
        if i == strip.numPixels()-1:
            for j in reversed(range(strip.numPixels())):
                strip.setPixelColor(j, color)
                strip.setPixelColor(j+1, 0)
                strip.show()
                time.sleep(wait_ms/1000.0)
        else:
            strip.setPixelColor(i, color)
            strip.setPixelColor(i-1, 0)
            strip.show()
            time.sleep(wait_ms/1000.0)

def tetris(strip,  wait_ms = 10):
    total = 0
    last = BLACK
    color = BLUE
    
    while total <= strip.numPixels():
        
        # Generate random size
        size = random.randint(3, 7)    
        
        # Choose random color
        color = random.choice(COLORS)
        if color == last:
            color = GRAY
        else:
            last = color
        
        # Draw shape
        for i in range(size+1):
            if i == 0:
                strip.setPixelColor(i, BLACK)
            else:
                strip.setPixelColor(i, color)
        strip.show()
        
        # Move shape down
        for j in range(strip.numPixels()-(total+size)):
            for i in reversed(range(1, strip.numPixels()-total)):
                strip.setPixelColor(i, strip.getPixelColor(i-1))
            strip.show()

        # Add size to total
        total = total + size

        #time.sleep(wait_ms/1000.0)

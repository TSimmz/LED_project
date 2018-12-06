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

def doubleWipe(strip0, strip1, color0, color1):
    """Wipes two colors across both displays"""
    j = strip0.numPixels()-1
    for i in range(strip0.numPixels()):
        strip0.setPixelColor(i, color0)
        strip1.setPixelColor(j, color1)
        strip0.show()
        strip1.show()
        j -= 1

    j = strip0.numPixels()-1
    for i in range(strip0.numPixels()):
        strip0.setPixelColor(i, color1)
        strip1.setPixelColor(j, color0)
        strip0.show()
        strip1.show()
        j -= 1

def colorSet(strip, color):
    """Set color across display entirely"""
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

def rainbowCycle(strip0, strip1, wait_ms=5, iterations=50):
    """Draw rainbow that uniformly distributes itself across all pixels."""
    for j in range(256*iterations):
        k = 255
        for i in range(strip0.numPixels()):
            strip0.setPixelColor(i, wheel((int(i * 256 / strip0.numPixels()) + j) & 255))
            strip1.setPixelColor(k, wheel((int(i * 256 / strip1.numPixels()) + j) & 255))
            k -= 1    
        strip0.show()
        strip1.show()
        time.sleep(wait_ms/1000.0)

def theaterChaseRainbow(strip0, strip1, wait_ms=50):
    """Rainbow movie theater light style chaser animation."""
    for j in range(256):
        for q in range(3):
            for i in range(0, strip0.numPixels(), 3):
                strip0.setPixelColor(i+q, wheel((i+j) % 255))
                strip1.setPixelColor(i+q, wheel((i+j) % 255))
            strip0.show()
            strip1.show()
            time.sleep(wait_ms/1000.0)
            for i in range(0, strip0.numPixels(), 3):
                strip0.setPixelColor(i+q, 0)
                strip1.setPixelColor(i+q, 0)

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
    """Flashes every 5th pixel - alternate red and green"""
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
    """Brightness from 0 to 255 of first 255 pixels - red"""
    for i in range(255):
        strip.setPixelColor(i, Color(i,0,i))
        strip.show()

def randomPixel(strip, color, wait_ms=5):
    """Lights a random pixel"""
    strip.setPixelColor(random.randint(0, strip.numPixels()), color)
    strip.show()
    time.sleep(wait_ms/1000.0)

def bounce(strip, color, wait_ms=0):
    """Bounces one pixel back and forth across strip"""
    bottom = strip.numPixels()/3
    top = bottom * 2
    for i in range(bottom, top):
        if i == top-1:
            for j in reversed(range(bottom, top)):
                strip.setPixelColor(j, color)
                strip.setPixelColor(j+1, 0)
                strip.show()
                #time.sleep(wait_ms/1000.0)
        else:
            strip.setPixelColor(i, color)
            strip.setPixelColor(i-1, 0)
            strip.show()
            #time.sleep(wait_ms/1000.0)

def tetris(strip,  wait_ms = 10):
    """Creates a 'shape' with random color and size and moves it down until strip is filled"""
    total = 0
    while total <= strip.numPixels():
        
        # Generate random size
        size = random.randint(3, 7)    
        
        # Choose random color
        color = wheel(random.randint(0,255))

        # Draw shape
        for i in range(size+1):
            if i == 0:
                strip.setPixelColor(i, BLACK)
            else:
                strip.setPixelColor(i, color)
        strip.show()
        
        # Move shape down
        for j in range(strip.numPixels()-(total+size)-1):
            for i in reversed(range(1, strip.numPixels()-total)):
                strip.setPixelColor(i, strip.getPixelColor(i-1))
            strip.show()

        # Add size to total
        total += size
           
def bounce_bar(strip, color, color2):
    
    val = random.randint(10,45)
    val2 = random.randint(25, strip.numPixels()/4)
    
    bottom = (strip.numPixels()/2) - val
    top = (strip.numPixels()/2) + val

    if val > 44:
        color = wheel(random.randint(0,255))
    
    if val2> 65:
        color2 = wheel(random.randint(0,255))

    for j in range(0, val2-1):
        strip.setPixelColor(j, color2)
    
    strip.setPixelColor(val2, RED)

    for j in range(val2+1, bottom-1):
        strip.setPixelColor(j, BLACK)    
    
    strip.setPixelColor(bottom, RED)

    for j in range(bottom+1, strip.numPixels()/2):
        strip.setPixelColor(j, color)
    
    for j in range(strip.numPixels()/2,top-1):
        strip.setPixelColor(j, color)

    strip.setPixelColor(top, RED)

    for j in range(top+1, strip.numPixels()-val2-1):
        strip.setPixelColor(j, BLACK)
    
    strip.setPixelColor(strip.numPixels()-val2, RED)

    for j in range(strip.numPixels()-val2+1, strip.numPixels()):
        strip.setPixelColor(j, color2)
        
def pulse(strip):
    for j in range(255):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, Color(j, 255, 0) )
        strip.show()
        time.sleep(1.0/1000.)

def police(strip0, strip1):
    half = strip0.numPixels()/2
    full = strip0.numPixels()
    for i in range(half):
        strip0.setPixelColor(i, BLUE)
        strip1.setPixelColor(i, RED)

    for i in range(half, full):
        strip0.setPixelColor(i, BLACK)
        strip1.setPixelColor(i, BLACK)

    strip0.show()
    strip1.show()
    time.sleep(100/1000.0)

    for i in range(half, full):
        strip0.setPixelColor(i, RED)
        strip1.setPixelColor(i, BLUE)

    for i in range(half):
        strip0.setPixelColor(i, BLACK)
        strip1.setPixelColor(i, BLACK)

    strip0.show()
    strip1.show()
    time.sleep(50/1000.0)

def police2(strip0, strip1):
    
    for i in range(strip0.numPixels()):
        strip0.setPixelColor(i, BLUE)
        strip1.setPixelColor(i, BLACK)

    strip0.show()
    strip1.show()
    time.sleep(0.75/10.0)

    for i in range(strip0.numPixels()):
        strip0.setPixelColor(i, BLACK)
        strip1.setPixelColor(i, RED)

    strip0.show()
    strip1.show()
    time.sleep(0.75/10.0)

COOLING = 55
SPARKING = 120
def fire(strip, num_led):
    heat = [i for i in range(num_led)]

    for i in range(num_led):
        heat[i] = heat[i] - random.randint(0, ((COOLING*10/num_led)+2))

    for i in reversed(range(num_led)):
        if i < 2:
            break

        heat[i] = (heat[i-1] + heat[i+2] + heat[i+2]) / 3

    
    if random.randint(0, 255) < SPARKING:
        y = random.randint(0,6)
        heat[y] = heat[y] + random.randint(160, 255)

    for i in range(num_led):
      pass

def rotate_3(strip0, strip1, c0, c1, c2, invert=False):
    one = strip0.numPixels()/3
    two = one * 2
    thr = strip0.numPixels()
 
    for i in range(0, one):
        strip0.setPixelColor(i, c0)
    for i in range(one, two):
        strip0.setPixelColor(i, c1)
    for i in range(two, thr):
        strip0.setPixelColor(i, c2)

    for i in range(0, one):
        strip1.setPixelColor(i, c0)
    for i in range(one, two):
        strip1.setPixelColor(i, c1)
    for i in range(two, thr):
        strip1.setPixelColor(i, c2)

    strip0.show()
    strip1.show()

    #time.sleep(1)
    
    for j in range(one):
        for p in range(thr):
            data0 = strip0.getPixels()
            data1 = strip1.getPixels()

            strip0.setPixelColor(p, data0[(p+1)%thr])
            strip1.setPixelColor(p, data1[(p+1)%thr])
        
        strip0.show()
        strip1.show()
        time.sleep(10/1000)









from machine import Pin
from neopixel import NeoPixel
import time
import random
import math

w = 8
h = 8
l = 2
j = 0

r = math.floor(random.random()*(w*h-1))

n = NeoPixel(Pin(13, Pin.OUT), w*h)

while True:
    for i in range(w*h-1):
        if (i+j)%(w*h) == r:
            l = l + 1
            r = math.floor(random.random()*(w*h-1))
        n.fill((0,0,0))
        n[r] = (32, 0, 0)
        for j in range(l):
            if ((i+j)%16) < w:
                n[(i+j)%(w*h)] = (2, 2, 0)
            else: 
                p = math.floor((i+j+15)/16)*16-((i+j)%w)-1
                try:
                    n[p%(w*h)] = (2, 2, 0)
                except Exception as e:
                    print("p=%d, l=%d, i=%d, j=%d" % (p, l, i, j))
        n.write()
        time.sleep(.1)


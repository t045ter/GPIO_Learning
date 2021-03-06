
from __future__ import division
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

GPIO_O = [7,11,12,13] #output pins
GOIO_I = [40]         #input pins

#Configure IO to out
for  x in GPIO_O:
  GPIO.setup(x , GPIO.OUT)


#'for loop count to 100 toggle pin out high
for x in xrange(0,127):
  GPIO.output(7,(x >> 0)%2)
  GPIO.output(11,(x >> 1)%2)
  GPIO.output(12,(x >> 2)%2)
  GPIO.output(13,(x >> 4)%2)
  time.sleep(1)

print('all done')

GPIO.cleanup()


########################playing



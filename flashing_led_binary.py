
from __future__ import division
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
#Configure IO to out
GPIO.setup(7, GPIO.OUT)   #LED1
GPIO.setup(11, GPIO.OUT)  #LED2
GPIO.setup(12, GPIO.OUT)  #LED3
GPIO.setup(13, GPIO.OUT)  #LED4

#'for loop count to 100 toggle pin out high
for x in xrange(0,100):
  GPIO.output(7,(x >> 0)%2)
  GPIO.output(11,(x >> 1)%2)
  GPIO.output(12,(x >> 2)%2)
  GPIO.output(13,(x >> 4)%2)
  time.sleep(1)

print('all done')

#testing
GPIO.cleanup()











print((count_1 >> 0)%2)
print((count_1 >> 1)%2)
print((count_1 >> 2)%2)
print((count_1 >> 4)%2)

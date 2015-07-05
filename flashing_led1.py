from __future__ import division
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

GPIO.setup(7, GPIO.OUT)  #D0
gpiocount_ = 1
timecount_ = 10
timex_ = float(1 / timecount_)
for x in range(timecount_):
  gpiocount_ = not(gpiocount_)
  time.sleep(timex_)
  GPIO.output(7,gpiocount_)


print('all done')
print(timex_)
GPIO.cleanup()












print((count_1 >> 0)%2)
print((count_1 >> 1)%2)
print((count_1 >> 2)%2)
print((count_1 >> 4)%2)

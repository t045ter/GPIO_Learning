import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.IN)
GPIO.setup(12,GPIO.IN)

def my_callback(channel):  
    print "Rising edge detected on SW2 - even though, in the main thread,"  
    print "we are still waiting for a falling edge - how cool?\n"  
  
print "Make sure you have a button connected so that when pressed"  
print "it will connect GPIO pin 11 (pin 16) to 0v\n"  
print "You will also need a second button connected so that when pressed"  
print "it will connect GPIO port 12 to 0v"  
raw_input("Press Enter when ready\n>")  

GPIO.add_event_detect(12, GPIO.RISING, callback=my_callback)  
  
try:  
    print "Waiting for falling edge on pin 11"  
    GPIO.wait_for_edge(11, GPIO.FALLING)  
    print "Falling edge detected. Here endeth the second lesson."  
  
except KeyboardInterrupt:  
    GPIO.cleanup()       # clean up GPIO on CTRL+C exit  
GPIO.cleanup()           # clean up GPIO on normal exit  

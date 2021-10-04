# Author: Eamon Cabral

# In this code we will explore a Pulse Width Modulation
# This will be done the Raspberry Pi 3 B GPIO pin 7
# The way to do this will be as it follows:

# First, we need to setup our GPIO pins as regular after importing all the necessary modules

# The output pin is setup as usual:
# GPIO.setup( CHANNEL , GPIO.OUT ) <- By channel we mean the GPIO-Pin

# Instead of setting the Pin "High" or "Low" we create an instance variable P
# we indicate in what channel and at what frequency this instance will be running:
# p = GPIO.PWM( CHANNEL, FREQUENCY ) <- Notice how we are using the PWM function now 

# To start an instance of PWM we use:
# p.start(dc) <- here we are using the duty cycle as input

# To dim or brighten the LED we will need to constantly change the duty cycle:
# p.ChangeDutyCycle(dc) <- with the Duty Cycle in as the input

# Similarly, we can change the frequency as per:
# Although this is not really that necessary, just bear in mind using reasonable frequencies
# p.ChangeFrequency(frequency)

# Finally, to stop the PWM, we simply use:
# p.stop()

# ** This code will serve as basis for our wind tunnel wind speed modulation **
# ====================================  Begin Code   ==================================== #

import time
import RPi.GPIO as GPIO
active_pin = 7              # Pin with output voltage 3.3Vdc
initial_frequency = 60      # Hz
initial_DC = 0           # Initial duty cycle to start instance, should begin with led light off

GPIO.setmode(GPIO.BOARD)
GPIO.setup(active_pin, GPIO.OUT)


p = GPIO.PWM(active_pin, initial_frequency) # Here we set our instance of PWM to 60 Hz (Cycles/sec)

p.start(0) # We begin our instance with a Duty Cycle of 0, naturally the LED will be off

# It is now time to use our while loop, to maintain our circuit working while we don't interrupt it


##print("\n\nUse 'p.ChangeDutyCycle(dc)' to your desired value in a range of 0-100\%")
##print("Use 'p.ChangeFrequency(freq)' to your desired value in a range of 0-60 Hz")
##print("Use 'p.stop()' to stop the pulse width modulation")
##print("Use 'GPIO.cleanup()' to reset the pins\n\n")

print("\n\nTo exit code type in 'Terminate code'\n")
print("To change Frequency and Duty Cycle type in 'Change Frequency'\n\n")
DC = input("Please indicate a numerical value [from 0 - 100%] for the Duty Cycle (Only): \n\n")

if DC.lower() == 'terminate code':
    exit()

# This elif line is new, eliminate if it doesn't work properly
elif DC.lower() == 'change frequency':
    freq = int(input("Provide Frequency value: "))
    DC = int(input("Provide new Duty Cycle value: "))
    p.ChangeFrequency(freq)
    p.ChangeDutyCycle(DC)

else:
    DC = int(DC)

try:    
    while DC in range(101):
        p.ChangeDutyCycle(DC)
        DC = input()
        if DC.lower() == 'terminate code':
            print("\n\n\t1000101___Code Terminated___1000111\n\n")
            break
        elif DC.lower() == 'change frequency':
            freq = int(input("Provide Frequency value: "))
            DC = int(input("Provide new Duty Cycle value: "))
            p.ChangeFrequency(freq)
            p.ChangeDutyCycle(DC)
        else:
            DC = int(DC)
            
except KeyboardInterrupt:
    pass

p.stop()
GPIO.cleanup()

# ===========================  End of Code   =========================== #

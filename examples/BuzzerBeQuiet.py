from machine import Pin, PWM
import time

buzzer = PWM(Pin(22)) #define PWM output pin GP22

def playtone(frequency): # function to play tone on buzzer with define frequency
    buzzer.duty_u16(5000)
    buzzer.freq(frequency)

def bequiet():	# Function to stop buzzer
    buzzer.duty_u16(0)

while True:
    #playtone(1865)
    #time.sleep(0.5)
    bequiet()
    #time.sleep(0.5)


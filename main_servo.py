from gpiozero import Servo, AngularServo
from time import sleep
"""
servo = Servo(12)  # Activation GPIO 12, attention: gpiozero utilise BCM
servo.min() # Position minimale
sleep(1) # Attente 1 seconde
servo.mid() # Position médiane
sleep(1)
servo.max() # Position maximale
sleep(1)
"""
base=AngularServo(12, min_angle=0, max_angle=180) # Activation GPIO 13
base.angle=45 # Position 0
sleep(1)
base.angle=90 # Position 90
sleep(1)
base.angle=180 # Position 180
sleep(1)
base.angle=0 # Position 0

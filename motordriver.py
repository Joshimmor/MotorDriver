from time import sleep
import RPi.GPIO as gpio

class motordriver:
    def __init__(self,pul,dir,ena):
        self.pul = pul
        self.dir = dir
        self.ena = ena
    motor_rotation_speed = .0000001
    current_position = 0
    max_position = 2500
    # Function measures given position to see if its in range
    # max range allow 180 degrees or Pi radians of movement from 0
    # 200 microsteps is on full rotation 
    # currently using a 25:1 gear ratio
    # estimated Position is entered in degrees
    def position_delta(self,estimated_position:float):
        estimated_position_steps = (estimated_position/1.8) *   25
        if(estimated_position >= 0):
            motor_max_delta = self.max_position - self.current_position
            if(estimated motor_max_delta ) 
        else:

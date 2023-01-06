from time import sleep
import RPi.gpio as gpio

class motordriver:
    def __init__(self,pul,_dir,ena):
        self.pul = pul
        self.dir = _dir
        self.ena = ena
    motor_rotation_speed = .0000001
    current_position = 0
    max_position = 2500
    # Function measures given position to see if its in range
    # max range allow 180 degrees or Pi radians of movement from 0
    # 200 microsteps is on full rotation 
    # currently using a 25:1 gear ratio
    # estimated Position is entered in degrees
    def position_delta(self,estimated_position:float):float:
        # how many step required to make move
        estimated_position_steps = (estimated_position/1.8) *   25
        # moving in the "positive" direction
        if(estimated_position >= 0):
            motor_max_delta = self.max_position - self.current_position
            # Legal move // with in the joints range 
            if(estimated_position_steps <= motor_max_delta):
                self.current_position = estimated_position_steps + self.current_position
                return estimated_position_steps
            # Illegal or Out of bounds call
            # move to largest point 180 degrees
            else:
                motor_max_delta = self.max_position - self.current_position
                self.current_position = self.max_position
                return motor_max_delta
        # move in "negative" direction
        else:
            # legal move
            if(abs(estimated_position_steps) <= self.current_position):
                self.current_position = self.current_position - abs(estimated_position_steps)
                return estimated_position_steps
            # Out of bounds move 
            else:
                motor_max_delta = -1 * self.current_position
                self.current_position = 0
                return motor_max_delta
    # movement request
    def motor_movement(self,estimated_position:):
        # set pins
        gpio.setmode(gpio.BCM)
        gpio.setup(self.pul, gpio.OUT)
        gpio.setup(self.dir, gpio.OUT)
        gpio.setup(self.ena, gpio.OUT)
        try:
            gpio.output(self.ena,gpio.HIGH)
            print('ENA set to HIGH - Controller Enabled')
            # caculate movement
            pos = self.position_delta(estimated_position)
            sleep(.5)
            # set direction
            if(pos > 0):
                gpio.output(self.dir,gpio.HIGH)
            else:
                gpio.output(self.dir,gpio.LOW)
            # move distance
            for i in range(abs(pos)):
                gpio.output(self.pul,gpio.HIGH)
                sleep(self.motor_rotation_speed)
                gpio.output(self.pul,gpio.LOW)
                sleep(self.motor_rotation_speed)
            gpio.output(self.ena, gpio.LOW)
            sleep(.5)
        finally:
            # clean up
            gpio.cleanup()
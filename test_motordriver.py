from motordriver import motordriver
try:
    # pul:int,_dir:int,ena:int
    driver = motordriver(17,27,22)
    print("[ Moving Motor to Max Range]")
    driver.motor_movement(180)
    print("[ Moving Motor to Min Range]")
    driver.motor_movement(-180)
    print("[ Complete ]")
except(e):
    print(e)
import time
from adafruit_motorkit import MotorKit

kit = MotorKit(64)

kit.motor1.throttle = 0
kit.motor2.throttle = 0

while True:
    print("Forward!")
    time.sleep(1)

    print("Speed up...")
    for i in range(0, 101):
        speed = i * 0.01
        kit.motor1.throttle = speed        
        kit.motor2.throttle = speed
        time.sleep(0.1)

    time.sleep(2)
    
    print("Slow down...")
    for i in range(100, -1, -1):
        speed = i * 0.01
        kit.motor1.throttle = speed        
        kit.motor2.throttle = speed
        time.sleep(0.1)
        
    print("Halt for a while!")
    time.sleep(3)        

    print("Backward!")
    time.sleep(1)

    print("Speed up...")
    for i in range(0, -101, -1):
        speed = i * 0.01
        kit.motor1.throttle = speed        
        kit.motor2.throttle = speed
        time.sleep(0.1)

    print("Slow down...")
    for i in range(-100, 1):
        speed = i * 0.01
        kit.motor1.throttle = speed        
        kit.motor2.throttle = speed
        time.sleep(0.1)

    print("Stop!")
    kit.motor1.throttle = 0    
    kit.motor2.throttle = 0
    time.sleep(5)

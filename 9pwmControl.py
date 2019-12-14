import time
import PWMServo

PWMServo.setServo(2, 1200, 200)
time.sleep(0.2)
PWMServo.setServo(2, 1700, 200)
time.sleep(0.2)
PWMServo.setServo(2, 1200, 200)
time.sleep(0.2)
PWMServo.setServo(2, 1700, 200)
time.sleep(0.2)
PWMServo.setServo(2, 1500, 100)
time.sleep(0.1)

import threading
import time

import smbus

import LeCmd
import PWMServo
import device

PWMServo.setServo(1, 1500, 500)
PWMServo.setServo(2, 1500, 500)
LeCmd.cmd_i001([500, 18, 1, 500, 2, 388, 3, 500, 4, 594, 5, 500, 6, 575, 7, 800, 8, 725, 9, 500, 10, 612, 11, 500,
                    12, 406, 13, 500, 14, 425, 15, 200, 16, 275, 17, 500, 18, 445])    # 立正

RED   = 1
GREEN = 2
BLUE  = 3
WHITE = 4

R_F = 550
G_F = 950
B_F = 1200
r_f = 70
g_f = 100
b_f = 130
r = 0
g = 0
b = 0

port = 1
bus = smbus.SMBus(port)
apds = device.APDS9960(bus)
apds.enableLightSensor()
    
def color_logic():
    global R_F, G_F ,B_F
    global r_f, g_f ,b_f
    global r , g , b
    global R , G , B
    global RED, GREEN, BLUE, WHITE
    if apds.getMode is False:
        time,sleep(0.005)
   
    r = (R - r_f) * 255 / (R_F - r_f)
    g = (G - g_f) * 255 / (G_F - g_f)
    b = (B - b_f) * 255 / (B_F - b_f)
#    print(r,g,b)
    if r > g:
        t = RED
        print(RED)
    else:
        t = GREEN
    if t == GREEN and g < b:
        t = BLUE
    if t == RED and r < b:
        t = BLUE
    
    if t == BLUE and b > 50:
        return t
    elif t == GREEN and g > 50:
        return t
    elif t == RED and r > 50:
        return t
    else:
        return 0   
    return 0
    
color = None
def fine_Apple():
    global color
    global RED, GREEN, BLUE, WHITE
    while True:
        if color == RED:
            color = None
            PWMServo.setServo(1, 1200, 200)
            time.sleep(0.2)
            PWMServo.setServo(1, 1700, 200)
            time.sleep(0.2)
            PWMServo.setServo(1, 1200, 200)
            time.sleep(0.2)
            PWMServo.setServo(1, 1700, 200)
            time.sleep(0.2)
            PWMServo.setServo(1, 1500, 100)
            time.sleep(0.1)
        elif color == GREEN or color == BLUE:
            color = None
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
        else:
            time.sleep(0.01)           

#启动动作运行子线程
th = threading.Thread(target=fine_Apple)
th.setDaemon(True)
th.start()

while True:
    time.sleep(0.25)
    R = apds.readRedLight()
    G = apds.readGreenLight()
    B = apds.readBlueLight()
    color = color_logic()
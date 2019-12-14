#! usr/bin/env python
# -*- coding:UTF-8 -*-
import math
import time

import LeCmd
import mpu6050

factor = 180 / math.pi
offset = None
radianX = 0.0
radianY = 0.0



def tumble():
#     if SSR.runningAction is False:
     if  radianX  > - 60 and radianX < -10 :
         time.sleep(2)
         LeCmd.cmd_i001([400, 16, 1, 500, 2, 500, 3, 303, 4, 500, 5, 500, 6, 650, 7, 762, 8,724,
            9, 500, 10, 500, 11, 696, 12,500, 13, 500, 14, 350, 15, 237, 16, 275])
         time.sleep(0.4)
         LeCmd.cmd_i001([400, 16, 1, 500, 2, 500, 3, 303, 4, 500, 5, 500, 6, 500, 7, 500, 8, 724,
            9, 500, 10, 500, 11, 696, 12, 500, 13, 500, 14, 500, 15, 500, 16, 275])
         time.sleep(0.4)
         LeCmd.cmd_i001([400, 16, 1, 500, 2, 500, 3, 303, 4, 500, 5, 500, 6, 800, 7, 200, 8, 353,
            9, 500, 10, 500, 11, 696, 12, 500, 13, 500, 14, 200, 15, 800, 16, 646])
         time.sleep(0.4)
         LeCmd.cmd_i001([400, 16, 1, 500, 2, 500, 3, 303, 4, 500, 5, 500, 6, 800, 7, 612, 8, 353,
            9, 500, 10, 500, 11, 696, 12, 500, 13, 500, 14, 200, 15, 387, 16, 646])
         time.sleep(0.4)
         LeCmd.cmd_i001([200, 16, 1, 500, 2, 500, 3, 303, 4, 500, 5, 500, 6, 800, 7, 612, 8, 353,
            9, 500, 10, 500, 11, 696, 12, 500, 13, 500, 14, 200, 15, 387, 16, 646])
         time.sleep(0.2)
         LeCmd.cmd_i001([500, 16, 1, 500, 2, 743, 3, 0, 4, 837, 5, 500, 6, 500, 7, 875, 8, 246,
            9, 500, 10, 256, 11, 1000, 12, 162, 13, 500, 14, 500, 15, 125, 16, 753])
         time.sleep(0.5)
         LeCmd.cmd_i001([500, 16, 1, 500, 2, 743, 3, 0, 4, 837, 5, 500, 6, 500, 7, 875, 8, 246,
            9, 500, 10, 256, 11, 1000, 12, 162, 13, 500, 14, 500, 15, 125, 16, 753])
         time.sleep(0.5)
         LeCmd.cmd_i001([700, 16, 1, 500, 2, 795, 3, 21, 4, 555, 5, 500, 6, 500, 7, 875, 8, 387,
            9, 500, 10, 212, 11, 978, 12, 448, 13, 500, 14, 500, 15, 125, 16, 612])
         time.sleep(0.7)
         LeCmd.cmd_i001([600, 16, 1, 500, 2, 500, 3, 303, 4, 500, 5, 500, 6, 537, 7, 800, 8, 724,
            9, 500, 10, 500, 11, 696, 12, 500, 13, 500, 14, 462, 15, 200, 16, 275])
         time.sleep(0.6)
         LeCmd.cmd_i001([400, 16, 1, 500, 2, 395, 3, 500, 4, 593, 5, 500, 6, 575, 7, 800, 8, 724,
            9, 500, 10, 605, 11, 500, 12, 406, 13, 500, 14, 425, 15, 200, 16, 275])
         time.sleep(0.4)
     elif radianY > 60:
         time.sleep(2)
         LeCmd.cmd_i001([500, 16, 1, 500, 2, 500, 3, 303, 4, 500, 5, 500, 6, 537, 7, 800, 8,724,
            9, 500, 10, 500, 11, 696, 12,500, 13, 500, 14, 462, 15, 200, 16, 275])
         time.sleep(0.5)
         LeCmd.cmd_i001([600, 16, 1, 500, 2, 508, 3, 683, 4, 857, 5, 500, 6, 537, 7, 800, 8,809,
            9, 500, 10, 517, 11, 303, 12,142, 13, 500, 14, 462, 15, 200, 16, 190])
         time.sleep(0.2)
         LeCmd.cmd_i001([700, 16, 1, 500, 2, 500, 3, 886, 4, 703, 5, 500, 6, 537, 7, 537, 8,809,
            9, 500, 10, 500, 11, 113, 12,296, 13, 500, 14, 462, 15, 462, 16, 190])
         time.sleep(0.2)
         LeCmd.cmd_i001([600, 16, 1, 500, 2, 406, 3, 471, 4, 143, 5, 500, 6, 481, 7, 125, 8,500,
            9, 500, 10, 593, 11, 528, 12,856, 13, 500, 14, 518, 15, 875, 16, 500])
         time.sleep(0.2)
         LeCmd.cmd_i001([400, 16, 1, 500, 2, 256, 3, 556, 4, 143, 5, 500, 6, 481, 7, 125, 8,387,
            9, 500, 10, 743, 11, 443, 12,856, 13, 500, 14, 518, 15, 875, 16, 612])
         time.sleep(0.2)
         LeCmd.cmd_i001([400, 16, 1, 500, 2, 275, 3, 471, 4, 143, 5, 500, 6, 481, 7, 800, 8,500,
            9, 500, 10, 725, 11, 528, 12,856, 13, 500, 14, 518, 15, 200, 16, 500])
         time.sleep(0.2)
         LeCmd.cmd_i001([900, 16, 1, 500, 2, 395, 3, 488, 4, 593, 5, 500, 6, 575, 7, 800, 8,724,
            9, 500, 10, 605, 11, 511, 12,406, 13, 500, 14, 425, 15, 200, 16, 275])
         time.sleep(0.2)
         
     
# 获得传感器的初始偏差，测量100次，取平均值
def get_offset():
    offset_ax = 0.0
    offset_ay = 0.0
    offset_az = 0.0
    offset_gx = 0.0
    offset_gy = 0.0
    offset_gz = 0.0
    global mpu
    for i in range(0, 100):
        a_date = mpu.get_accel_data(g=True)
        g_date = mpu.get_gyro_data()
        offset_ax += a_date['x']
        offset_ay += a_date['y']
        offset_az += a_date['z']
        offset_gx += g_date['x']
        offset_gy += g_date['y']
        offset_gz += g_date['z']
    return {'ax': offset_ax/100, 'ay': offset_ay/100, 'az': offset_az/100 - 1,
            'gx': offset_gx/100, 'gy': offset_gy/100, 'gz': offset_gz/100}


def get_gm(m):
    global mpu
    global gx
    global gy
    global gz
    global t
    # global dt
    global offset
    if m == 'x':
        gyro_date = mpu.get_gyro_data()
        gx += (gyro_date['x'] - offset['gx']) * (time.time() - t)
        t = time.time()
        return gx
    elif m == 'y':
        gyro_date = mpu.get_gyro_data()

        gy += (gyro_date['y'] - offset['gy']) * (time.time() - t)
        t = time.time()
        return gy
    elif m == 'z':
        gyro_date = mpu.get_gyro_data()
        gz += (gyro_date['z'] - offset['gz']) * (time.time() - t)
        t = time.time()
        return gz



mpu = mpu6050.mpu6050(0x68)
mpu.set_gyro_range(mpu.GYRO_RANGE_2000DEG)
mpu.set_accel_range(mpu.ACCEL_RANGE_2G)
LeCmd.cmd_i001([500, 18, 1, 500, 2, 388, 3, 500, 4, 594, 5, 500, 6, 575, 7, 800, 8, 725, 9, 500, 10, 612, 11, 500,
                    12, 406, 13, 500, 14, 425, 15, 200, 16, 275, 17, 500, 18, 445])    # 立正
offset = get_offset()

last_ang_R = 0
last_ang_P = 0
if __name__ == '__main__':
    t = time.time()
    while True:
        accel_date = mpu.get_accel_data(g=True)
        gyro_date = mpu.get_gyro_data()
        
        try:
            ax = accel_date['x'] - offset['ax']
            ay = accel_date['y'] - offset['ay']
            az = accel_date['z'] - offset['az']
            gx = gyro_date['x'] - offset['gx']
            gy = gyro_date['y'] - offset['gy']
            angle_x = math.atan2(ax, az)
            angle_y = math.atan2(ay, az)
            
            radianX = angle_y * factor
            radianY = angle_x * factor
            print(radianX)
            
            tumble()
        except:
            pass
        time.sleep(0.05)

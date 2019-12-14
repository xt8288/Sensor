#!/usr/bin/env python3
# -*- coding:UTF-8 -*-
import threading
import time

import LeCmd
import hcsr04

LeCmd.cmd_i001([500, 18, 1, 500, 2, 388, 3, 500, 4, 594, 5, 500, 6, 575, 7, 800, 8, 725, 9, 500, 10, 612, 11, 500,
                    12, 406, 13, 500, 14, 425, 15, 200, 16, 275, 17, 500, 18, 445])    # 立正
distance_ok = False
distance = 0.0

GPIO_TRIG = 20  # 超声波trig引脚对应的IO号
GPIO_ECHO = 21   # 超声波echo引脚对应的IO号

sonar = hcsr04.Measurement(GPIO_TRIG, GPIO_ECHO)

def move():
    global distance
    global distance_ok
    while True:
        print(distance)
        if distance_ok:
            if distance < 20.0 or distance == 0:
                LeCmd.cmd_i001([100, 16, 1, 500, 2, 395, 3, 488, 4, 593, 5, 500, 6, 575, 7, 800, 8, 724,
                9, 518, 10, 605, 11, 511, 12,406, 13, 443, 14, 425, 15, 200, 16, 275])
                time.sleep(0.1)
                LeCmd.cmd_i001([100, 16, 1, 500, 2, 395, 3, 488, 4, 593, 5, 500, 6, 575, 7, 800, 8, 724,
                9, 447, 10, 605, 11, 511, 12,406, 13, 443, 14, 425, 15, 200, 16, 275])
                time.sleep(0.1)
                LeCmd.cmd_i001([100, 16, 1, 500, 2, 395, 3, 488, 4, 593, 5, 500, 6, 575, 7, 800, 8, 724,
                9, 500, 10, 605, 11, 511, 12,406, 13, 500, 14, 425, 15, 200, 16, 275])
                time.sleep(0.1)
                LeCmd.cmd_i001([100, 16, 1, 500, 2, 395, 3, 488, 4, 593, 5, 500, 6, 575, 7, 800, 8, 724,
                9, 518, 10, 605, 11, 511, 12,406, 13, 443, 14, 425, 15, 200, 16, 275])
                time.sleep(0.1)
                LeCmd.cmd_i001([100, 16, 1, 500, 2, 395, 3, 488, 4, 593, 5, 500, 6, 575, 7, 800, 8, 724,
                9, 447, 10, 605, 11, 511, 12,406, 13, 443, 14, 425, 15, 200, 16, 275])
                time.sleep(0.1)
                LeCmd.cmd_i001([100, 16, 1, 500, 2, 395, 3, 488, 4, 593, 5, 500, 6, 575, 7, 800, 8, 724,
                9, 500, 10, 605, 11, 511, 12,406, 13, 500, 14, 425, 15, 200, 16, 275])
                time.sleep(0.1)

                distance_ok = False
            else:
                LeCmd.cmd_i001([500, 18, 1, 500, 2, 388, 3, 500, 4, 594, 5, 500, 6, 575, 7, 800, 8, 725, 9, 500, 10, 612, 11, 500,
                    12, 406, 13, 500, 14, 425, 15, 200, 16, 275, 17, 500, 18, 445])    # 立正
                distance_ok = False
        else:
            time.sleep(0.01)


th1 = threading.Thread(target=move)
th1.setDaemon(True)     # 设置为后台线程，这里默认是False，设置为True之后则主线程不用等待子线程
th1.start()


while True:
    if distance_ok is False:
        try:
            distance = sonar.distance_metric(sonar.raw_distance(2, 0.08))
            if distance_ok is False:
                distance_ok = True
        except:
            pass  
    else:
        time.sleep(0.01)

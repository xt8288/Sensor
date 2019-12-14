# encoding: utf-8
'''
Company: 深圳市幻尔科技有限公司
官网:hiwonder.com
日期:2019/9/20
by Aiden
'''

#四路巡线传感器使用例程
import time

import smbus


class LineFollower:

    # Global Variables
    address = None
    bus = None

    def __init__(self, address, bus=1):
        self.address = address
        self.bus = smbus.SMBus(bus)

    def readData(self, register):
        value = self.bus.read_byte_data(self.address, register)
        return value

if __name__ == "__main__":
    addr = 0x78 #巡线传感器iic地址
    line = linefollower(addr)
    reg = 0x01
    while 1:
        data = line.readData(reg)
        #0表示识别到黑线，1表示没有识别到黑线
        print("Sensor1:", data & 0x01, " Sensor2:", (data >> 1) & 0x01, " Sensor3:", (data >> 2) & 0x01, " Sensor4:", (data >> 3) & 0x01)
        time.sleep(0.5)

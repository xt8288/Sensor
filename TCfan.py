import time

import RPi.GPIO as GPIO
import smbus

GPIO.setmode(GPIO.BCM)
GPIO_M = 9
GPIO_m = 10

class Aht10():
    address = None
    bus = None
              
    def __init__(self, address, bus=1):
        self.address = address
        self.bus = smbus.SMBus(bus)
        
    def GetHumidity(self):
        value = self.readSensor(True)
        if value == 0:
            return 0
        return value * 100 / 1048576
    
    def GetTemperature(self):
        value = self.readSensor(False)
        return ((200 * value) / 1048576) - 50
        
    def readStatus(self):
        result = self.bus.read_byte(self.address)
#        print(result)
        return result
        
    def writeByte(self):
        self.bus.write_i2c_block_data(self.address, 0, [0xE1, 0x08, 0x00])
        time.sleep(0.5)
        if (Aht10.readStatus(self) & 0x68) == 0x08:
            return True
        else:
            return False
        
    def readSensor(self,GetDataCmd):
        self.bus.write_i2c_block_data(self.address, 0, [0xAC, 0x33, 0x00])
        time.sleep(0.1)

        temp = self.bus.read_i2c_block_data(self.address, 0)[0:6]
        print(temp)                   
        if GetDataCmd is True:
            result = ((temp[1] << 16) | (temp[2] << 8) | temp[3]) >> 4
        else:
            result = ((temp[3] & 0x0F) << 16) | (temp[4] << 8) | temp[5]
        return result
    
    def Reset(self):
        self.bus.write_byte(self.address,0xBA)
        time.sleep(0.02)
        
if __name__ == '__main__':
    addr = 0x38
    AHT10 = Aht10(addr)
    print(AHT10.writeByte())
    while True:
        print('Humidity = {}℃'.format(AHT10.GetHumidity()))
        print('Temperature = {}%'.format(AHT10.GetTemperature()))
        Temperature = AHT10.GetTemperature()
        Humidity = AHT10.GetHumidity()
        if Temperature > 25:
            GPIO.setup(GPIO_M, GPIO.OUT)
            GPIO.output(9, 1)
            time.sleep(1)
        else :
            GPIO.setup(GPIO_M, GPIO.OUT)
            GPIO.output(9, 0)
            time.sleep(1)
        time.sleep(0.5)
        
        
        
        
        
        
        
        
        
        
        

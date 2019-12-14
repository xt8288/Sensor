import time

import smbus


class Aht10():
    address = None
    bus = None
    CT_data = []
    c1 = 0
    t1 = 0
    AHT10_I2C_ADDR = 0x38
        
    def __init__(self, address, bus=1):
        self.address = address
        self.bus = smbus.SMBus(bus)
        
    def JH_Send_AC(self):
        self.bus.write_byte(self.address,0xac)
        self.bus.write_byte(self.address,0x33)
        self.bus.write_byte(self.address,0x00)
        
    def JH_Send_BA(self):
        self.bus.write_byte(self.address,0xBA)
        
    def JH_Read_Status(self):
        self.bus.write_byte(0x38,1)
#        Byte_first = self.bus.read_byte(self.address)
        Byte_first = self.bus.read_byte(self.address)
        print(Byte_first)
        return Byte_first     
        
    def JH_Read_Cal_Enable(self):
        
        if (Aht10.JH_Read_Status(self) & 0x68) == 0x08:
            return 1
        else:
            return 0
        
    def JH_Init(self):
#        self.bus.write_byte(self.address,0xe1)
#        self.bus.write_byte(self.address,0x08)
#        self.bus.write_byte(self.address,0x00)
#        time.sleep(0.5)
#        
        count = 0
        while self.JH_Read_Cal_Enable() == 0:
#            time.sleep(0.1)
#            print(4444)
            self.bus.write_byte(self.address,0xe1)
            self.bus.write_byte(self.address,0x08)
            self.bus.write_byte(self.address,0x00)
            
            count += 1
            if count >= 10:
                return 0
#            time.sleep(0.5)
        return 1
    
    def JH_Read_CTdata(self):
        buf = [0, 0]
        Byte_1th = 0
        Byte_2th = 0
        Byte_3th = 0
        Byte_4th = 0
        Byte_5th = 0
        Byte_6th = 0
        Retudata = 0
        cnt = 0
        Aht10.JH_Send_AC(self)
        time.sleep(0.075)
        while (self.JH_Read_Status() & 0x80) ==0x80:
            print(1111)
            time.sleep(0.02)
            cnt = cnt + 1
            if cnt >100:
                break
        cnt = 0

        for i in range(6):
            
            if cnt ==0:
                Byte_1th = self.bus.read_byte(self.address)
            if cnt ==1:
                Byte_2th = self.bus.read_byte(self.address)
            if cnt ==2:
                Byte_3th = self.bus.read_byte(self.address)
            if cnt ==3:
                Byte_4th = self.bus.read_byte(self.address)
            if cnt ==4:
                Byte_5th = self.bus.read_byte(self.address)
            if cnt ==5:
                Byte_6th = self.bus.read_byte(self.address)
            cnt += 1
            
        Retudata = (Retudata | Byte_2th) << 8
        Retudata = (Retudata | Byte_3th) << 8
        Retudata = (Retudata | Byte_4th) 
        Retudata = Retudata >> 4
        buf[0] = Retudata
        Retudata = 0
        Retudata = (Retudata | Byte_4th) << 8
        Retudata = (Retudata | Byte_5th) << 8
        Retudata = (Retudata | Byte_6th)
        Retudata = Retudata & 0xfffff
        buf[1] = Retudata
        
        return buf

if __name__ == '__main__':
    addr = 0x38
    AHT10 = Aht10(addr)
    AHT10.JH_Init()
    AHT10.JH_Read_Status()
    
#    print(AHT10.write_(1))
#    while True:
#        while AHT10.JH_Read_Cal_Enable() == 0:
#           AHT10.JH_Init()
#           print(3333)
#           time.sleep(0.03)
##        print(2222)
#        b0, b1 = AHT10.JH_Read_CTdata()
#        c1 = b0 * 1000 /1024 /1024
#        t1 = b1 *200 * 10 / 1024 /1024 - 500
#    #    print(buf[0])
#        print('H = {}'.format(c1))
#        print('T = {}'.format(t1))
#        time.sleep(1)
    
    
    
           
    
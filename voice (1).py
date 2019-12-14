import time

import smbus


class Voice:
      
    address = None
    bus = None
    TTS_MODULE_I2C_ADDR =  0x40

    def __init__(self, address, bus=1):
        self.address = address
        self.bus = smbus.SMBus(bus)
    
    def WireReadTTSDataByte(self):
        val = self.bus.read_byte(self.address)
        return True
    
    def TTSModuleSpeak(self, sign, words):
        head = [0xFD,0x00,0x00,0x01,0x00]
#        
        wordslist = words.encode("gb2312")
        print(wordslist)
        length = len(wordslist) + 2    
        print(length)
#        length = len(signdata) + len(wordslist) + 2
        head[1] = length >> 8
        head[2] = length
        head.extend(list(wordslist))
        print(head)
        self.bus.write_i2c_block_data(self.address, 0, head) 
        #self.bus.write_i2c_block_data(self.address, 0, [0,])     
        #self.bus.write_i2c_block_data(self.address, 0, list(wordslist))
        time.sleep(0.05)
        
if __name__ == '__main__':
        addr = 0x40
        v = Voice(addr)
        v.TTSModuleSpeak("[h0]","hello")

  











        
        
        
        

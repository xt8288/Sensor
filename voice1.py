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
#        signdata = []       
#        for i in range(0, len(sign)):
#            signdata.append(eval(hex(ord(sign[i]))))
#            print(eval(hex(ord(words[i]))))
            
        wordslist = []       
        for i in range(0, len(words)):
            wordslist.append(eval(hex(ord(words[i]))))
            print((hex(ord(words[i]))))
        length = len(wordslist) + 2    
#        length = len(signdata) + len(wordslist) + 2
        head[1] = length >> 8
        head[2] = length
        print(head)
        self.bus.write_i2c_block_data(self.address, 0, head) 
#        self.bus.write_i2c_block_data(self.address, 0, signdata)     
        self.bus.write_i2c_block_data(self.address, 0, wordslist)
        time.sleep(0.05)
        
if __name__ == '__main__':
        addr = 0x40
        v = Voice(addr)

        v.TTSModuleSpeak('',"1,1")

  











        
        
        
        
import time

import smbus  # 调用树莓派IIC库


class Voice:
      
    address = None
    bus = None
    TTS_MODULE_I2C_ADDR =  0x40 #传感器的IIC地址

    def __init__(self, address, bus=1):
        self.address = address
        self.bus = smbus.SMBus(bus)
    
    def WireReadTTSDataByte(self):
        val = self.bus.read_byte(self.address)
        return True
    
    def TTSModuleSpeak(self, sign, words):
        head = [0xFD,0x00,0x00,0x01,0x00]             #文本播放命令
        wordslist = words.encode("gb2312")            #将文本编码格式设为GB2312
        signdata = sign.encode("gb2312")    
        length = len(signdata) + len(wordslist) + 2
        head[1] = length >> 8
        head[2] = length
        head.extend(list(signdata))
        head.extend(list(wordslist))        
        self.bus.write_i2c_block_data(self.address, 0, head) #向从机发送数据
        time.sleep(0.05)
        
if __name__ == '__main__':
        addr = 0x40
        v = Voice(addr)
        v.TTSModuleSpeak("[h0][v10][m55]","你好，我叫Q bot")   #[h0]设置单词发音方式，0为自动发音 [v10]设置音量，音量范围为0-10,10为最大音量。[m54]选择发音人

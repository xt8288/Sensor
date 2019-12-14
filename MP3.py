# encoding: utf-8
#使用例程
import time

import smbus


class MP3:

    # Global Variables
    address = None
    bus = None

    MP3_PLAY_NUM_ADDR        = 1 #指定曲目播放，0~3000，低位在前，高位在后
    MP3_PLAY_ADDR            = 5 #播放
    MP3_PAUSE_ADDR           = 6 #暂停
    MP3_PREV_ADDR            = 8 #上一曲
    MP3_NEXT_ADDR            = 9 #下一曲
    MP3_VOL_VALUE_ADDR       = 12 #指定音量大小0~30
    MP3_SINGLE_LOOP_ON_ADDR  = 13 #开启单曲循环,要在播放过程开启才有效
    MP3_SINGLE_LOOP_OFF_ADDR = 14 #关闭单曲循环

    def __init__(self, address, bus=1):
        self.address = address
        self.bus = smbus.SMBus(bus)        
        
    def play(self):
        self.bus.write_byte(self.address, self.MP3_PLAY_ADDR)
        time.sleep(0.02)
        
    def pause(self):
        self.bus.write_byte(self.address, self.MP3_PAUSE_ADDR)
        time.sleep(0.02)
        
    def prev(self):
        self.bus.write_byte(self.address, self.MP3_PREV_ADDR)
        time.sleep(0.02)
        
    def next(self):
        self.bus.write_byte(self.address, self.MP3_NEXT_ADDR)
        time.sleep(0.02)
        
    def loopOn(self):
        self.bus.write_byte(self.address, self.MP3_SINGLE_LOOP_ON_ADDR)
        time.sleep(0.02)
        
    def loopOff(self):
        self.bus.write_byte(self.address, self.MP3_SINGLE_LOOP_OFF_ADDR)
        time.sleep(0.02)

    def playNum(self, num):
        self.bus.write_word_data(self.address, self.MP3_PLAY_NUM_ADDR, num)
        time.sleep(0.02)
        
    def volume(self, value):
        self.bus.write_word_data(self.address, self.MP3_VOL_VALUE_ADDR, value)
        time.sleep(0.02)
            
if __name__ == "__main__":
    addr = 0x7b #传感器iic地址
    mp3 = MP3(addr)
    mp3.volume(15) #设置音量为20，注意在播放前设置
    mp3.playNum(2) #播放歌曲3
#    mp3.loopOn() #设置为单曲循环，注意在播放中设置
    time.sleep(60) #延时，验证是否单曲循环中，延时时间应该大于歌曲时间长度
    mp3.loopOff() #关闭循环，如果在歌曲播放中关闭，歌曲会播放完整后才停下
#    mp3.volume(30) 
    mp3.play() #播放
    time.sleep(2)
#    mp3.next() #切到下一首，即歌曲序号加1
#    time.sleep(2)
#    mp3.prev() #切回上一首，即歌曲序号减1
#    time.sleep(2)
    mp3.pause() #暂停


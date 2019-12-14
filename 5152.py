import array
import time

from event import *


class XFSCommand():
    XFS_H = 0XFD
    XFS_CMOS = {
            "play":0x01,
            "stop":0x02,
            "pause":0x03,
            "resume":0x04,
            "state":0x21,
            "sleep":0x88,
            "weakup":0xFF,
            "senbtobuf":0x31,
            "playbuf":0x32
            }

    XFS_BACK = {
            "init ok":0x4A,
            "com ok":0x41,
            "com err":0x45,
            "busy":0x4E,
            "notbusy":0x4F
            }
    txt_encode_params = {
            "gb2312":0x00,
            "gbk":0x01,
            "big5":0x02,
            "unicode":0x03
            }
    def __init__(self):
        pass
    
    def print_cmd_hex(self,cmd):
        dat = "".join(map(lambda x: (''if len(hex(x))>=4 else '0')+hex(x)[2:],cmd))
        print(dat)
    
    def cmd_play(self,_str,_encode):
        pd = array.array('B')
        arraydata = _str.encode(_encode)
        datalen = len(arraydata)
        if (datalen>1024*4):
            return pd
            pass
        reallen = datalen + 2
        pd.append(self.XFS_H)
        
        if (reallen > 0xff):
            pd.append(reallen >> 8)
            pd.append(reallen&0xff)
        else:
            pd.append(0x00)
            pd.append(reallen)
        pd.append(self.XFS_COMS["play"])
        pd.append(self.txt._encode_params[_encode])

        for i in range(datalen):
            pd.append(arraydata[i])
        return pd
        pass
    def cmd_stop(self):
        return self.cmd_1_byte("stop")
    
    def cmd_pause(self):
        return self.cmd_1_byte("pause")
    
    def cmd_resume(self):
        return self.cmd_1_byte("resume")
   
    def cmd_state(self):
        return self.cmd_1_byte("state")
    
    def cmd_sleep(self):
        return self.cmd_1_byte("sleep")
    
    def cmd_weakup(self):
        return self.cmd_1_byte("weakup")
    
    def cmd_1_byte(self,_n):
        pd = array.array('B')
        pd.append(self.XFS_H)
        pd.append(0x00)
        pd.append(0x01)
        pd.append(self.XFS_COMS[_n])
        return pd
        pass
    
if __name__ == '__main__':
    #
    
    a=u'科大讯飞'
    print(a.encode())
    utf8_a=bytearray(a,"utf-8")
    gb2312_a=a.encode("gb2312")
    gbk_a = a.encode("gbk")
 
    print(utf8_a)
    print(gb2312_a)
    print(gbk_a)
    #big5_a = a.encode('big5')
    #print(unicode(s, 'big5'))
    #print(big5_a)
 
    print("-------------")
    cmdObj = XFSCommand()
 
    #print(cmdObj.cmd_1_byte("pause"))
    #print(cmdObj.XFS_COMS["pause"])
    #print(cmdObj.cmd_pause())
    cmdObj.print_cmd_hex(cmdObj.cmd_pause())
    cmdObj.print_cmd_hex(cmdObj.cmd_play("科大讯飞", "gb2312"))
    cmdObj.print_cmd_hex(cmdObj.cmd_play("科大訊飛", "big5"))
    #
    while 1:
        time.sleep(1)


    
    
    
    
    
    
    
    




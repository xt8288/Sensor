import smbus


class Voice:
      
    address = None
    bus = None
    TTS_MODULE_I2C_ADDR =  0x40

    def __init__(self, address, bus=1):
        self.address = address
        self.bus = smbus.SMBus(bus)
        self.bus.write_i2c_block_data(self.address, 0, [0xFD,0x00,0x02,0x01,0x01])
        print('ok')
    
a = Voice(0x40)

from I2C_device import *
import time
 
class Board:
    def __init__(self, addr=0x48, port=1):
        self.device = I2C_device(addr, port)
 
    def custom(self):
        self.device.write_cmd(0x00)
        self.device.read()
        return self.device.read()
 
    def control(self):
        self.device.write_cmd(0x01)
        self.device.read()
        return self.device.read()
 
    def light(self):
        self.device.write_cmd(0x02)
        self.device.read()
        return self.device.read()
 
    def temperature(self):
        self.device.write_cmd(0x03)
        self.device.read()
        return self.device.read()
 
    def output(self, val):
        self.device.write_cmd_arg(0x40, val)
 
def main():
    board = Board()
    print "%s: control:%d light:%d temp:%d custom:%d" % (time.asctime(),board.control(),board.light(),board.temperature(),board.custom())
    temp = "The room temperature is %d on %s:" % (board.temperature(),time.asctime())
    file = open("/home/pi/homepi/temperature-sensor/sensor.txt","w")
    file.write(temp)
    file.close()
    print temp
    time.sleep(5)
       
 
if __name__ == "__main__":
    main()
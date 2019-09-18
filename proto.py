from time import sleep
import gpio
import smbus
import logger

RST = 24

#i2c addresses
device_address = 0x49

virt_hwh = 0x00
virt_hwl = 0x01
virt_swh = 0x02
virt_swl = 0x03

class Triad():
     def __init__(self, i2c=1):
          self.bus = smbus.SMBus(i2c)
          gpio.set_value(RST, 1)
          self.device_address = 0x49
          self.device_reg_status = 0x00
          self.device_reg_write = 0x01
          self.device_reg_read = 0x02

          self.enable_triad()
          

     def read_reg(self, virt_reg):
          self.bus.write_byte_data(self.device_address,
                                   self.device_reg_write,
                                   virt_reg)
          
          return self.bus.read_byte_data(self.device_address,
                                         self.device_reg_read)
     def write_reg(self, virt_reg, data):
          self.bus.read_byte_data(self.device_address,
                                   self.device_reg_write,
                                   virt_reg)
          
          return self.bus.write_byte_data(self.device_address,
                                          self.device_reg_write)

     def enable_triad(self):
          try:
               gpio.enable_gpio(RST)
          except:
               print("GPIO already enabled")
          
          # enable gpio 20-whatever
          gpio.set_direction(RST,"out")
          # set direction - out
          # set reset - "1"
          gpio.set_value(RST, int(1))
          
     
     def read_status(self):
          return self.bus.read_byte_data(self.device_address, self.device_reg_status)

status = logger.Logger("results.txt")                                        



if __name__ == "__main__":
     triad = Triad()
     status = logger.Logger("results.txt")
     
     print(triad.read_status())
     status.log(triad.read_reg(21))

     status.log("Register, Data")

     try:
       for i in range(0x56):
            status.log("0x{:02x}, 0x{:02x}".format(i, triad.read_reg(i)))
            sleep(.1)
     finally:
          status.close()

     # Can read the data in python with
     # data = np.loadtxt("results.txt", skiprows=1, delimiter=',')

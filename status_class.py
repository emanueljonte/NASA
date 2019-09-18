from time import sleep
import gpio
import smbus
import triad

#i2c addresses
device_address = 0x49

virt_hwh = 0x00
virt_hwl = 0x01
virt_swh = 0x02
virt_swl = 0x03

class Triad():
     def __init__(self, i2c=1):
          self.bus = smbus.SMBus(i2c)
          self.gpio.set_value(RST, 1)
          #TODO: Add GPIO Toggling Make sure RST=1
          self.device_address = 0x49
          self.device_reg_status = 0x00
          self.device_reg_write = 0x01
          self.device_reg_read = 0x02

     def read_reg(self, virt_reg):
          self.bus.write_byte_data(self.device_address,
                                   self.device_reg_write,
                                   virt_reg)
          
          return self.bus.read_byte_data(self.device_address,
                                         self.device_reg_read)
     def write_reg(self, virt_reg, data):
          pass
     
     def read_status(self):
          return self.bus.read_byte_data(self.device_address,
                                         self.device_reg_status)

#print("It works!!")
#
#
#try:
#     gpio.enable_gpio(RST)
#     
#except:
#     print("GPIO already enabled")
#
#sleep (0.5)
#gpio.set_direction(RST,"out")
#        
#gpio.set_value(RST,0)

#bus = smbus.SMBus(1)

#print("Printing Status")
#for i in range(5):
#    status = read_status()
#    print(bin(status))
#    sleep(1)

#print("\nPrinting Registers")

#for i in range(0x55):
    #print("Addr: 0x{:02x} Data: 0x{:02x}".format(i, read_reg(i)))
    #sleep(.1)
#status = bus.read_byte_data(device_address, device_reg_status)
#write = bus.write_byte_data(device_address, device_reg_write,0x00)
#read = bus.read_byte_data(device_address, device_reg_read)


if __name__ == "__main__":
     triad = Triad()
     print(triad.read_status())

     for i in range(0x56):
          print("Addr: 0x{:02x} Data: 0x{:02x}".format(i, triad.read_reg(i)))
          sleep(.1)

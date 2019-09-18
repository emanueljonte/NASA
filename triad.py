from time import sleep
import gpio
import smbus
import sys

RST = 24
INT = 23

if __name__ == "__main__":
        print("Hello")
        try:
           gpio.enable_gpio(RST)
        
                # enable rst
                # set output
                
                # enable int
                # set input
        except:
               print("GPIO already enabled")

        sleep (0.1)
        gpio.set_direction(RST,"out")
        
        gpio.set_value(RST, int(1))


        #try:
        #         gpio.enable_gpio(INT)
        #                         
        #except:
        #        print("GPIO already enabled")
        #
        #sleep (0.5)
        #gpio.set_direction(INT,"in")


        
      #  gpio.set_value(RST, TRIAD_RST)

                
        
        # set rst to 1 (this takes it out of reset)

        # set up i2c

        # reading values from triad
        
#print(dir(gpio))

from time import sleep


def enable_gpio(x):
    with open("/sys/class/gpio/export", 'w') as fp:
        fp.write(str(x))

def set_direction(x, direction):
    with open("/sys/class/gpio/gpio{}/direction".format(x), 'w') as fp:
        if direction:
            fp.write("out")
        else:
            fp.write("in")
            
            
def set_value(x, val):
    with open("/sys/class/gpio/gpio{}/value".format(x), 'w') as fp:
        fp.write(str(val))
    
def get_value(x):
    pass

#def val(x):
#    with open("/sys/class/gpio/gpio{}/direction".format(x), 'w') as fp:
#        fp.write((val))

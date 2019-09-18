import status_class
import smbus

x = "Driver"

y = "Value"

print (x , y)

if __name__ == "__main__":
    triad = Triad()
    print(triad.read_status())
    
    for i in range(0x56):
        print("Addr: 0x{:02x} Data: 0x{02x}".format(i, triad.read_reg(i)))
        sleep(.1)




print ("Driver, Value", file = open("results.py", "a"))

o = open("results.py", "a")
print("Driver, Value", file = o)
o.close()

with open ("results.py", "a") as o:
    print("Driver, Value", file = o)

# Way 1
with open ("results.txt", "a") as fp:
    fp.write("Register: {}, Value: {}".format(a, b))

# Way 2
fp = open ("results.txt", "a")

# heres some stuff
for i in range(10):
    fp.write(str(i))
# more stuff

fp.close()

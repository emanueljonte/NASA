class Logger():
    def __init__(self, filename):
        self.fp = open(filename, 'w')


    def log(self, messege):
        self.fp.write(messege+"\n")


    def close(self):
        self.fp.close()

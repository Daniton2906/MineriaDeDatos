import sys

class Printer:

    def __init__(self, max_amount, size=None):
        self.n = max_amount
        if size is not None:
            self.size = size
        else:
            self.size = 10
        self.delta = int(self.n / self.size)
        self.k = -1
        self.closed = False
        self.update()


    def update(self):
        if not self.closed:
            self.k += 1
            if self.is_update_time():
                b = " [" + "|" * int(self.k / self.delta) + " " * int(10 - (self.k / self.delta)) + "]"
                sys.stdout.write('\r' + b)

    def is_update_time(self):
        return self.k%self.delta == 0

    def reset(self, max_amount):
        self.n = max_amount
        self.delta = int(self.n / self.size)
        self.k = -1
        self.closed = False
        self.update()

    def close(self):
        print ""
        self.closed = True

from compare import *

class MyArrayList:

    def __init__(self):
        self.array = []
        self.n = 0

    def get_length(self):
        return self.n

    def compare(self, element1, element2):
        c1 = int(element1[0])
        c2 = int(element2[0])
        return (c2 - c1) / max(abs(c2 - c1), 1)

    def add_repeat(self, index):
        self.array[index][1] += 1

    def map(self, element):
        return [element[0], 1]

    def insert(self, element):
        i = 0
        if self.n == 0:
            self.array.append(self.map(element))
        else:
            j = self.n - 1
            while i <= j:
                m = int(i + (j - i) / 2)
                aux = self.array[m]
                if self.compare(aux, element) < 0:
                    j = m - 1
                elif self.compare(aux, element) > 0:
                    i = m + 1
                else:
                    self.add_repeat(m)
                    return m
            self.array.insert(i, self.map(element))
        self.n += 1
        return i

    def sort(self, compare=None):
        if compare is not None:
            sorted(self.get_list(), key=cmp_to_key(compare))

    def get_list(self):
        return self.array

    def toLine(self, i):
        L = self.get_list()
        return L[i][0]+","+str(L[i][1])+"\n"
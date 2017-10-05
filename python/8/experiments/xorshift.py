class XORShift:
    def __init__(self, rnd):
        self.rnd = rnd

    def get_random(self):
        self.rnd ^= (self.rnd << 21)
        self.rnd ^= (self.rnd >> 35)
        self.rnd ^= (self.rnd << 4)
        a = str(self.rnd)
        return a[int(a[4]): int(a[4])+5]


d = {}

a = XORShift(111111111111111)
count = 0
for i in range(1000):
    rez = a.get_random()
    if not d.get(rez, 0):
        d[rez] = 1
    else:
        count += 1
        print(rez)
        d[rez] += 1


print(count)
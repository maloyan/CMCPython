class Dots:
    def __init__(self, start, end):
        self.start = start
        self.end   = end
    def __getitem__(self, n):
        if type(n) is int:
            arr = []
            for i in range(n):
                arr.append(self.start + i * (float) (self.end - self.start) / (n - 1))
            return arr
        elif type(n) is slice:
            if n.step == None:
                step = (float) (self.end - self.start) / (n.stop - 1) 
                return self.start + n.start * step
            else:
                st = n.start
                en = n.stop
                if n.start == None:
                    st = 0
                if n.stop == None:
                    en = n.step
                step = (float) (self.end - self.start) / (n.step - 1)
                return [self.start + i * step for i in range(st, en)]



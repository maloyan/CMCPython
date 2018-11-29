class DivStr :
    def __init__(self, string):
        self.string = string
    def __floordiv__(self, other):    
        size = len(self.string) // other
        arr = []
        for i in range(other):
            word = ""
            for j in range(i*size, (i+1)*size):
                word += self.string[j]
            arr.append(word)
        return arr
    def __mod__(self, other):
        size = len(self.string) % other
        if size != 0:
            return self.string[-size:]
        else:
            return ""

#a = DivStr("XcDfQWEasdERTdfgRTY")
#print(*a//4)
#print(a%4)


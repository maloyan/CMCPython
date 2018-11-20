class vector:
    def __init__(self, arr):
        self.arr = arr
    def __add__(self, other):
        ans = []
        if not isinstance(other, vector):
            other = vector(other)
        for i in range(len(self.arr)):
            ans.append(self.arr[i] + other.arr[i])
        return vector(ans)
    def __radd__(self, other):
        ans = []
        if not isinstance(other, vector):
            other = vector(other)
        for i in range(len(self.arr)):
            ans.append(self.arr[i] + other.arr[i])
        return vector(ans)           
    def __str__(self):
        line = ''
        for i in range(len(self.arr)):
            if i != len(self.arr) - 1:
                line += str(self.arr[i]) + ':'
            else: 
                line += str(self.arr[i])
        return line

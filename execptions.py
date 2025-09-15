class Stack:
    def __init__(self, sz):
        self.size = sz
        self.arr = []
        self.top = -1   # corrected name

    def push(self, n):
        if self.top + 1 == self.size:
            raise IndexError("Stack is full")
        self.top += 1
        self.arr.append(n)

    def pop(self):
        if self.top == -1:
            raise IndexError("Stack is empty")
        n = self.arr[self.top]
        self.arr.pop()
        self.top -= 1
        return n

    def printall(self):
        print(self.arr)


# Test
s = Stack(5)

s.push(10)
print(s.pop())   # should print 10

# this will raise error because stack is empty now
# print(s.pop())

s.push(20)
s.push(30)
s.push(40)
s.push(50)
s.push(60)

s.printall()

# This will raise "Stack is full"
s.push(70)
class MinStack(object):
    def __init__(self):
        self.stack = []
        
    def push(self, x):
        self.stack.append((x, min(self.getMin(), x))) 
           
    def pop(self):
        self.stack.pop()

    def top(self):
        if self.stack:
            return self.stack[-1][0]
        
    def getMin(self):
        if self.stack:
            return self.stack[-1][1]
        return float('inf')        

	def __str__(self):
		return str(self.elements)

el = [1, 3, 7, 10]
stack = MinStack(el)
stack.push(5)
print(stack)
stack.pop()
print(stack)
print(stack.top())
print(stack.getMin())


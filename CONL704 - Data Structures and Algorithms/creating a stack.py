
 #Creating a stack in python

class Stack:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    
    def peek(self):
        return self.items[-1]
    def pop (self):
        self.items.pop()
    def push(self, item):
        self.items.append(item)
    def size(self):
        return len(self.items)
    

# test styak functions
testo = Stack()
testo.push('a')
testo.push('b')
testo.push('c')

print(testo.peek())
testo.pop()
print(testo.peek())
print(testo.size())
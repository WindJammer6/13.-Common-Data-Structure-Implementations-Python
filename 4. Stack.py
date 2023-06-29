from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()

    def push(self,value):
        self.container.append(value)

    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return self.container[-1]
    
    def is_empty(self):
        return len(self.container) == 0
    
    def size(self):
        return len(self.container)
    
    def __repr__(self):
        return '{}'.format(self.container)
    

if __name__ == '__main__':
    stack = Stack()

    stack.push(5)

    print(stack.peek())

    print(stack.pop())
    print(stack)

    print(stack.is_empty())

    stack.push(67)
    stack.push(7)
    stack.push(748)

    print(stack.size())
    print(stack)

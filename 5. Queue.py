from collections import deque

class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self,value):
        self.buffer.appendleft(value)

    def dequeue(self):
        return self.buffer.pop()
    
    def is_empty(self):
        return len(self.buffer) == 0
    
    def size(self):
        return len(self.buffer)

    def front_element(self):
        return self.buffer[-1]
    
    def last_element(self):
        return self.buffer[0]
    
    def __repr__(self):
        return '{}'.format(self.buffer)
    

if __name__ == '__main__':
    queue = Queue()

    queue.enqueue({    
        'company':'Walmart',
        'timestamp': '15 apr, 11.01am',
        'price': 131.10
    })

    print(queue.dequeue())
    print(queue)

    print(queue.is_empty()) 

    queue.enqueue({    
        'company':'Walmart',
        'timestamp': '15 apr, 11.01am',
        'price': 131.10
    })
    queue.enqueue({    
        'company':'Walmart',
        'timestamp': '15 apr, 11.02am',
        'price': 131.12
    })
    queue.enqueue({    
        'company':'Walmart',
        'timestamp':'15 apr, 11.03am',
        'price': 135
    })

    print(queue.front_element())
    print(queue.last_element())
    
    print(queue.dequeue())
    print(queue.size())
    print(queue)

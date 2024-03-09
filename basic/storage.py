from queue import PriorityQueue as PQ

class Queue:
    def __init__(self):
        self.queue = []


    def push(self, item):
        self.queue.append(item)


    def pop(self):
        if (self.is_empty()):
            return None
        else:
            return self.queue.pop(0)


    def is_empty(self):
        return len(self.queue) == 0
    

class PriorityQueue:
    def __init__(self):
        self.queue = PQ()


    def push(self, valor, item):
        self.queue.put((valor, item))


    def pop(self):
        if (self.is_empty()):
            return None
        else:
            (_, node) = self.queue.get()
            return node


    def is_empty(self):
        return self.queue.empty()


class Stack:
    def __init__(self):
        self.stack = []


    def push(self, item):
        self.stack.append(item)


    def pop(self):
        if (self.is_empty()):
            return None
        else:
            return self.stack.pop()


    def is_empty(self):
        return len(self.stack) == 0
    
    
    def length(self):
        return len(self.stack)
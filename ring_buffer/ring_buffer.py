class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.container = []
        self.age = 0

    def append(self, item):
        if len(self.container) != self.capacity:
            self.container.append(item)
        else:
            if self.age == self.capacity:
                self.age = 0
                self.container[self.age] = item
                self.age += 1
            else:
                self.container[self.age]= item
                self.age += 1 
                            
    def get(self):
        return self.container
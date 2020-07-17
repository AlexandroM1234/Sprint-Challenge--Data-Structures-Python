class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.container = []

    def append(self, item):
        if len(self.container) != self.capacity:
            self.container.append(item)
        else:
            self.container.clear()
            self.append(item)
                            
    def get(self):
        return self.container
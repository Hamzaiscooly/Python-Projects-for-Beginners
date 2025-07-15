# Custom Iterator

class Counter:
    def __init__(self, limit):
        self.limit = limit
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.limit:
            self.count += 1
            return self.count
        raise StopIteration

for num in Counter(5):
    print(num)
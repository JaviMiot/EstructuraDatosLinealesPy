
class ListQueue:
    def __init__(self):
        self.items = []
        self.size = len(self.items)

    def enqueue(self, data):
        self.items.insert(0, data)

    def dequeue(self):
        data = self.items.pop()
        return data

    def traverse(self):

        for item in self.items:
            print(item)

    def getSize(self):
        self.size = len(self.items)


food = ListQueue()
food.enqueue('eggs')
food.enqueue('ham')
food.enqueue('spam')
print(food.dequeue())
print('Que tiene el Queue')
food.traverse()

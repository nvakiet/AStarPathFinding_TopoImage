import heapq
import itertools

class FrontierQueue():
    "A priority queue to use as the frontier for A* search algorithm, if 2 items have same priority, it will pop out using FIFO rule"
    REMOVED = (-1,-1) # Invalid coordinate to mark a removed item
    def __init__(self):
        self.priorityQueue = []
        self.entryDict = {}
        self.counter = itertools.count()

    def push(self, item, priority=0):
        "Add new item to queue or change priority of existing item"
        if item in self.entryDict:
            self.remove(item)
        count = next(self.counter)
        entry = [priority, count, item]
        self.entryDict[item] = entry
        heapq.heappush(self.priorityQueue, entry)

    def remove(self, item):
        "Mark item as removed in the dictionary"
        entry = self.entryDict.pop(item)
        entry[-1] = self.REMOVED

    def pop(self):
        "Remove and return the item with lowest priority"
        while self.priorityQueue:
            priority, count, item = heapq.heappop(self.priorityQueue)
            if item is not self.REMOVED:
                del self.entryDict[item]
                return item
        return None

    def hasItem(self, item):
        "Check if an item is already in the queue"
        return item in self.entryDict

    def getPriority(self, item):
        "Return the current priority of the item in the queue"
        entry = self.entryDict[item]
        return entry[0]
from heapq import heapify, heappop, heappush

class MaxHeap:
    def __init__(self):
        self.heap = []
    
    def parent(self, i):
        return int((i-1)/2)
    
    def insertKey(self, k):
        heappush(self.heap, -k)
    
    def increaseKey(self, i, new):
        self.heap[i] = new
        while (i!=0 and self.heap[self.parent(i)] > self.heap[i]):
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
        
    def extractMax(self):
        return heappop(self.heap)

    def deleteKey(self, i):
        self.increaseKey(i, float("inf"))
        self.extractMax()
    
    def getMax(self):
        return self.heap[0]

maxHeap = MaxHeap()
maxHeap.insertKey(5)
maxHeap.insertKey(3)
maxHeap.insertKey(17)
maxHeap.insertKey(10)
maxHeap.insertKey(84)
maxHeap.insertKey(19)
maxHeap.insertKey(6)
maxHeap.insertKey(22)
maxHeap.insertKey(9)

print("The Max val is " + str(-1*maxHeap.extractMax()))
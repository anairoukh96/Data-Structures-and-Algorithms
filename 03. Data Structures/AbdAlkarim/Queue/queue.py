# Queue
# Queue
# Queue
# Queue  implementation for call center 

class Queue():
    def __init__(self, k):
        self.k = k
        self.queue = [None] * k
        self.head = self.tail = -1

    # Insert an element into the queue
    def enqueue(self, data):
        if (self.tail == self.k - 1):
            print("The queue is full\n")

        elif (self.head == -1):
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = data
        else:
            self.tail = self.tail + 1
            self.queue[self.tail] = data

    # Delete an element from the queue
    def dequeue(self):
        if (self.head == -1):
            print("The queue is empty\n")

        elif (self.head == self.tail):
            temp = self.queue[self.head]
            self.head = -1
            self.tail = -1
            return temp
        else:
            temp = self.queue[self.head]
            self.head = self.head + 1
            return temp

    def printQueue(self):
        if(self.head == -1):
            print("No element in the queue")

        else:
            for i in range(self.head, self.tail + 1):
                print(self.queue[i], end=" ")
            print()

#  Queue Example object will be instantiated and called as such:
obj = Queue(5)
obj.enqueue("scme.edu.ps")
obj.enqueue("login.scme.edu.ps")
obj.enqueue("google.com")
obj.enqueue("youtube.com")
obj.enqueue("079833333")
print("Initial queue")
obj.printQueue()

obj.dequeue()
print("After removing an element from the queue")
obj.printQueue()


class Node:
    def __init__(self,val):
        self.value = val
        self.next = None
    
        
class Queue:
    def __init__(self,val):
        new_node = Node(val)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def printqueue(self):
        temp = self.first
        while temp != None:
            print(temp.value,end="->")
            temp = temp.next


    def enqueue(self,val):
        new_node = Node(val)
        if self.length == 0:
            self.first = new_node
            self.last = new_node
        elif self.length == 1:
            self.last = new_node
            self.first.next = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length+=1

    def dequeue(self):
        temp = self.first
        if not self.first:
            return None
        elif self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = temp.next
            temp.next = None
        self.length-= 1
        return temp

my_queue = Queue(4)
my_queue.printqueue()
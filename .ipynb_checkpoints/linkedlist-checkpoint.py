class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,value) -> None:
        self.newnode = Node(value)
        self.head = self.newnode
        self.tail = self.newnode
        self.length = 1

    def append(self,value):
        self.newnode = Node(value)
        self.tail.next = self.newnode
        self.tail = self.newnode
      

linked_list = LinkedList(4)
print(linked_list.head.value)
print(linked_list.tail.value)
linked_list = LinkedList.append(5)
print(linked_list.head.value)
print(linked_list.tail.value)
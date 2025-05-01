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
    
    def print_list(self):
        temp = self.head
        if temp == None:
            print("Empty list")
        while temp is not None:
            print(temp.value,end="->")
            temp = temp.next
        print()
    
    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0
        print("List is empty now.")
    
    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length +=1
        return True
    def pop(self):
        if self.head == None:
            return None
        elif self.head == self.tail:
            self.make_empty()
        else:
            temp = self.head
            while temp.next != self.tail:
                temp = temp.next
            self.tail=temp
            self.tail.next = None
            self.length-=1
            return temp
    def prepend(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        # elif self.head == self.tail:
        #     self.head = new_node
        #     self.head.next = self.tail
        # else:
        #     temp = self.head
        #     self.head = new_node
        #     self.head.next = temp
        else:
            new_node.next = self.head
            self.head = new_node
        self.length+=1
        return True
    def pop_first(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            self.head = self.tail = None
        else:
            temp = self.head
            self.head = self.head.next
        self.length-=1
        return temp     
    def get(self,index):
        temp = self.head
        if self.length == 0:
            return None
        if self.length <= index or index<0:
            return None
        for _ in range(index):
            temp = temp.next
        return temp
    def set_value(self,index,value):
        temp = self.head
        if index < 0 or index >= self.length:
            return False
        else:
            for _ in range(index):
                temp = temp.next
            temp.value = value
            return True 
    def insert(self,index,value):
        new_node = Node(value)
        temp = self.head
        # if index <0:
        #     new_node.next = self.head
        #     self.head = new_node
        # elif index >= self.length:
        #     self.tail.next = new_node
        #     self.tail = new_node
        if index <0 or index > self.length:
            return False
        elif index == 0:
            return self.prepend(value)
        elif index == self.length:
           return  self.append(value)
        else:
            for _ in range(index):
                pre = temp
                temp = temp.next
            new_node.next = temp
            pre.next = new_node
            self.length+=1
            return True
    def remove(self,index):
        if index <0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length-1:
            return self.pop()
        pre = self.get(index-1)
        temp = pre.next
        pre.next = temp.next
        temp.next=None
        self.length-=1
        return temp
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
       

linked_list = LinkedList(4)
linked_list.append(5)
linked_list.append(18)
linked_list.append(20)
linked_list.append(38)
# linked_list.print_list()
# print(f"Head is: {linked_list.head.value}")
# print(f"Tail is: {linked_list.tail.value}")
# print(f"Length of list is: {linked_list.length}")
# print("\nAfter pop function")
# linked_list.pop()
# linked_list.print_list()
# print(f"Head is: {linked_list.head.value}")
# print(f"Tail is: {linked_list.tail.value}")
# print(f"Length of list is: {linked_list.length}")
linked_list.prepend(54)
print(f"Head is: {linked_list.head.value}")
print(f"Tail is: {linked_list.tail.value}")
# print(f"Length of list is: {linked_list.length}")
# linked_list.print_list()
#linked_list.pop_first()
# print(f"Head is: {linked_list.head.value}")
linked_list.print_list()
print(f"Length of list is: {linked_list.length}")
# print(linked_list.get(4))
# print(linked_list.remove(3))
linked_list.reverse()
linked_list.print_list()
# print(f"Length of list is: {linked_list.length}")
print(f"Head is: {linked_list.head.value}")
print(f"Tail is: {linked_list.tail.value}")

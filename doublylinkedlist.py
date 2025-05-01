class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.next = None
        self.prev = None
class DoublyLinkedList:
    def __init__(self,value) -> None:
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value,end="<->")
            temp = temp.next
    def emptymylist(self):
        self.head = None
        self.tail = None
        self.length = 0
    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.length+=1
        return True
    def pop(self):
        if self.head is None:
            return None
        elif self.head.next == None:
            temp = self.head
            self.emptymylist()
            return temp
        else:
            temp = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length-=1
        return temp
    def preappend(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.length+=1
        return True
    def popFirst(self):
        if self.length == 0:
            return None
        elif self.length ==1:
            temp = self.head
            self.emptymylist()
            return temp
        else:
            temp = self.head
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length-=1
        return temp 
    def get(self,index):
        if self.length == 0 or index<0 or index>=self.length:
            return None
        elif self.head.next == None:
            return self.head
        else:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            return temp
    def setnode(self,index,value):
        if index<0 or index>self.length:
            return None
        else:
            temp = self.get(index)
            temp.value = value
            return True
    def insert(self,index,value):
        if index<0 or index>self.length:
            return None
        elif index == 0:
             return self.preappend(value)
        elif index == self.length:
            return self.append(value)
        else:
            new_node = Node(value)
            before = self.get(index-1)
            after = before.next
            new_node.prev = before
            new_node.next = after
            before.next = new_node
            after.prev = new_node
        self.length+=1
        return True
    def remove(self,index):
        if index<0 or index>self.length:
            return None
        elif index == 0:
             return self.popFirst()
        elif index == self.length-1:
            return self.pop()
        else:
            temp = self.get(index)
            before = temp.prev
            after = temp.next
            before.next = after
            after.prev = before
            temp.prev = None
            temp.next = None
        self.length-=1
        return temp
    #swap first and last node value without changing there pointer values
    def swap_first_last(self):
        if self.length<=0:
            return False
        temp = self.head.value
        self.head.value = self.tail.value
        self.tail.value = temp

    #reverse list 
    def reverse(self):
        if self.length<=0:
            return False
        elif self.head == self.tail:
            return True
        else:
            before = None
            temp = self.head
            after = temp.next
            for _ in range(self.length-1):
                temp.next = before
                temp.prev = after
                before = temp
                temp = after
                after = after.next
            temp.next = before
            temp.prev  = None
            self.tail = self.head
            self.head = temp
        #palindrom or not 
        def is_palindrome(self):
            left = self.head
            right = self.tail
            for _ in range(self.length//2):
                if left.value != right.value:
                    return False
                else:
                    left = left.next
                    right = right.prev
            return True
        





myDoublyList = DoublyLinkedList(5)
myDoublyList.append(10)
myDoublyList.append(12)
myDoublyList.append(92)
myDoublyList.append(52)
print(myDoublyList.remove(4))
myDoublyList.print_list()
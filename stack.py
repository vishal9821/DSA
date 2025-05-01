#node custructure

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class Stack:
    def __init__(self):
        new_node = Node(1)
        self.length = 1
        self.top = new_node

    def printStack(self):
        temp = self.top
        while temp!=None:
            print(temp.val,end="->")
            temp = temp.next
        print('\n')
    
    def push(self,val):
        new_node = Node(val)
        new_node.next = self.top
        self.top = new_node
        self.length+=1

    def pop(self):
        if  not self.top:
            return 
        elif not self.top.next:
            self.top = None
        else:
            temp = self.top
            self.top = temp.next
            temp.next = None
        self.length-=1
        return print(f'Removed Value is {temp.val}')



Stackcheck = Stack()
Stackcheck.push(2)
Stackcheck.push(3)
Stackcheck.printStack()
Stackcheck.pop()
Stackcheck.printStack()

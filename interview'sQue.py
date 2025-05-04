class Stack:
    def __init__(self):
        self.stack_list = []

    def print_stack(self):
        for i in range(len(self.stack_list)-1, -1, -1):
            print(self.stack_list[i])

    def is_empty(self):
        return len(self.stack_list) == 0

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list.pop()


def is_balanced_parentheses(val:str):
    data = val.replace('',' ').split()
    my_stack = Stack()
    for i in data:
        if i == '(':
            my_stack.push(i)
        else:
            if my_stack.pop():
                continue
            else:
                return False
    if my_stack.is_empty():
        return True
    else:
        return False
   
    
def reverse_string(string:str):
    mystr = list(string)
    mystack = Stack()
    revstr = []
    for i in mystr:
        mystack.push(i)
    for i in range(mystack.size()):
        char = mystack.pop()
        revstr.append(char)
    print(''.join(revstr))

# def sort_stack(obj:Stack):
#     if obj.is_empty():
#         return None
#     else:
#         sorted_stack = Stack()
#         while not obj.is_empty():
#             temp = obj.pop()
#             if sorted_stack.is_empty():
#                 sorted_stack.push(temp)
#             else:
#                 if temp < sorted_stack.peek():
#                     obj.push(sorted_stack.pop())
#                     while not sorted_stack.is_empty():
#                         if temp < sorted_stack.peek():
#                             obj.push(sorted_stack.pop())
#                         else:
#                             break
#                     sorted_stack.push(temp)
#                 else:
#                     sorted_stack.push(temp)
#         while not sorted_stack.is_empty():
#             temp = sorted_stack.pop()
#             obj.push(temp)
#         return obj
                         
def sort_stack(obj:Stack):
    additional_stack = Stack()
 
    while not obj.is_empty():
        temp = obj.pop()
 
        while not additional_stack.is_empty() and additional_stack.peek() > temp:
            obj.push(additional_stack.pop())
 
        additional_stack.push(temp)
 
    while not additional_stack.is_empty():
        obj.push(additional_stack.pop())
    return obj.print_stack()


#Queue implementaion using stack(using list)

class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        
    def enqueue(self, value):
        while len(self.stack1) > 0:
            self.stack2.append(self.stack1.pop())
        self.stack1.append(value)
        while len(self.stack2) > 0:
            self.stack1.append(self.stack2.pop())

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            temp = self.stack1.pop()
            return temp

    def peek(self):
        return self.stack1[-1]

    def is_empty(self):
        return len(self.stack1) == 0


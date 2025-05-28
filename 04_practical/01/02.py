class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item) 

    def pop(self):
        if not self.is_empty():
            return self.items.pop()  
        else:
            return "Stack is empty"

    def peek(self):
        if not self.is_empty():
            return self.items[-1] 
        else:
            return "Stack is empty"

    def is_empty(self):
        return len(self.items) == 0  

    def __str__(self):
        return str(self.items)

stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)
print("Stack:", stack)        

print("Top:", stack.peek())   

print("Popped:", stack.pop())  
print("Stack:", stack)         

print("Is empty?", stack.is_empty())  

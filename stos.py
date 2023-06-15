
class Stack():
    def __init__(self):
        self.stack = list()
    
    def push(self, element):
        self.stack.append(element)
        
    def __str__(self):
        return str(self.stack)

    def pop(self):
        if len(self.stack) >= 1:
            print(self.stack.pop())
            
        else:
            print("you are silly bro")

my_stack = Stack()
my_stack.push(11)
my_stack.push('charmander')
my_stack.push('czarizard')
my_stack.pop()
print(my_stack)

# print(my_stack.stack, my_stack.age, my_stack.color)

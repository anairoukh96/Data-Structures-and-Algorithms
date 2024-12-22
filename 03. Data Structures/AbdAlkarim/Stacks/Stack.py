def create_stack():
    stack = []
    return stack

def check_empty(stack):
    return len(stack) == 0

def push(stack, item):
    stack.append(item)
    print("pushed item: " + item)

def pop(stack):
    if check_empty(stack):
        return "Stack is empty"
    
    return stack.pop()

# Test the stack operations
stack = create_stack()
push(stack, str("scme.edu.ps"))
push(stack, str("login.scme.edu.ps"))
push(stack, str("google.com"))
push(stack, str("youtube.com"))
print("popped item: " + pop(stack))
print("stack after popping an element: " + str(stack))
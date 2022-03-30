from inspect import stack

def create_stack():
    stack = []
    return stack

def check_empty(stack):
    return len(stack) == 0

def push(stack, item):
    stack.append(item)
    print("push item : " + item)


def pop(stack):
    if(check_empty(stack)):
        return "stack is empty"

    return stack.pop()


stack = create_stack()
push(stack, str('*'))
push(stack, str('E'))
push(stack, str('A'))
push(stack, str('*'))
push(stack, str('C'))


print("popped : " + pop(stack))
print("stack after popping element : " + str(stack))
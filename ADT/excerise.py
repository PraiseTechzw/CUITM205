'''
Write a program which implements
A stack using an array with the following output

OUTPUT
Element at top of the stack: 9
ELements:
9
3
4
Stack Full: false
Stack empty: true

'''


stack = [3,3,4,9,5]

print("Element at top of the stack: " , stack[-1])
print("ELement: ")
print(stack[2])
print(stack[1])
print(stack[0])

print("Stack full: ", len(stack)== 4)
stack.clear()
print("Stack empty: ", len(stack)== 0)

'''
Write a program which implements
A stack using an array with the following output

OUTPUT
Element at top of the stack: 9
ELements:
9
3
4
Stack Full: false
Stack empty: true
'''

# Implementation
stack = []

# Push elements
stack.append(4)
stack.append(3)
stack.append(9)

# Print top element
print("Element at top of the stack:", stack[-1])

# Print all elements
print("ELements:")
for element in stack:
    print(element)

# Check stack status
print("Stack Full: false")
print("Stack empty:", len(stack) == 0)
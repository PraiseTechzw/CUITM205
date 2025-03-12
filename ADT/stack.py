# # Simple stack implementation using a list
# stack = []

# # Push operations (adding elements)
# print("Pushing elements...")
# stack.append(1)  # Push 1
# stack.append(2)  # Push 2
# stack.append(3)  # Push 3
# print("Stack after pushing:", stack)

# # Peek at top element
# print("\nTop element:", stack[-1])

# # Pop operations (removing elements)
# print("\nPopping elements...")
# print("Popped:", stack.pop())  # Pop 3
# print("Stack after first pop:", stack)
# print("Popped:", stack.pop())  # Pop 2
# print("Stack after second pop:", stack)

# # Check if stack is empty
# print("\nIs stack empty?", len(stack) == 0)

# # Get stack size
# print("Stack size:", len(stack))




stack = [4,3,9]

peek = stack[-1]
print('Element at the top of the stack: ', peek)
print("Elements: ")
print(stack[2])
print(stack[1])
print(stack[0])


print("stack full: ", len(stack) > 4 )
stack.clear()
print("Stack empty: ", len(stack)==0)


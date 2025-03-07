# Simple stack implementation using a list
stack = []

# Push operations (adding elements)
print("Pushing elements...")
stack.append(1)  # Push 1
stack.append(2)  # Push 2
stack.append(3)  # Push 3
print("Stack after pushing:", stack)

# Peek at top element
print("\nTop element:", stack[-1])

# Pop operations (removing elements)
print("\nPopping elements...")
print("Popped:", stack.pop())  # Pop 3
print("Stack after first pop:", stack)
print("Popped:", stack.pop())  # Pop 2
print("Stack after second pop:", stack)

# Check if stack is empty
print("\nIs stack empty?", len(stack) == 0)

# Get stack size
print("Stack size:", len(stack))


from collections import deque

queue = deque([1,2,3,4,5])

queue.append(6)

print("After appending:", queue)

queue.popleft()

print("After appending left:", queue)


print(queue)
print("Is queue empty?", len(queue) == 0)

print("Queue size:", len(queue))













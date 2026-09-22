from collections import deque
queue = deque()
n = int(input("How many numbers: "))
for i in range(n):
    num = int(input("Enter number: "))
    queue.append(num)
print("Queue:", queue)
while queue:
    print("Processing:", queue.popleft())

from collections import deque
queue=deque()
queue.append("A")
queue.append("B")
queue.append("C")
print("Queue: ",queue)
while queue:
    person=queue.popleft()
    print("processing:",person)
print("Queue after processing: ",queue)    
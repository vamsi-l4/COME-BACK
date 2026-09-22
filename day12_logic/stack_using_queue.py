from collections import deque
queue=deque()
nums = list(map(int,input("enter the nums: ").split()))
for value in nums:
    queue.append(value)
    for i in range(len(queue)-1):
        queue.append(queue.popleft())
print("stack: ",queue)
from collections import deque
queue=deque()
def push(val):
    queue.append(val)
    for i in range(len(queue)-1):
        queue.append(queue.popleft())
def pop():
    if len(queue)==0:
        print("stack is empty")        
    else:
        print("removed",queue.popleft())
def top():
    if len(queue)==0:
        print("stack is empty")        
    else:
        print("Top",queue[0])
push(1)
push(2)
push(3)

print(queue)

top()
pop()
top()
pop()
top()
pop()               
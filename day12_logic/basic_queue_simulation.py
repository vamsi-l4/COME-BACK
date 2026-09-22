from collections import deque
queue=deque()
queue.append("A")
queue.append("B")
queue.append("C")
queue.popleft()
queue.append("D")
queue.popleft()
print("Queue: ",queue)

from collections import deque
printer_queue = deque()
printer_queue.append("Document1")
printer_queue.append("Document2")
printer_queue.append("Document3")
print("print queue",printer_queue)
while printer_queue:
    job=printer_queue.popleft()
    print("printing:",job)
print("ALL jobs completed.")
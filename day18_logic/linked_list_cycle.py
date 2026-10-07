class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
nums=list(map(int,input("enter the nums: ").split()))
head=None
tail=None
for num in nums:
    new_node=Node(num)
    if head is None:
        head=new_node
        tail=new_node
    else:
        tail.next=new_node
        tail=new_node
tail.next=head.next
slow=head
fast=head
while fast is not None and fast.next is not None:
    slow=slow.next
    fast=fast.next.next
    if slow is fast:
        print('cycle detected')
        break
else:
    print('no cycle detected')
    
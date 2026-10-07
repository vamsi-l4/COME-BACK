class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
nums=list(map(int,input("enter the nums: ").split()))
target=int(input("enter target: "))
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
while head is not None and head.data==target:
    head=head.next
current=head
while current is not None and current.next is not None:
    if current.next.data==target:
        current.next=current.next.next
    else:
        current=current.next
current=head
while current is not None:
    print(current.data,end='->')
    current=current.next
print("None")
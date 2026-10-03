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
target=int(input("enter the target:"))
current=head
found=False
while current is not None:
    if current.data == target:
        found=True
        break
    current=current.next
if found:
    print("found")
else:
    print("not found")
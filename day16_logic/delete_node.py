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
target=int(input("enter the delete num: "))
current=head
previous=None
while current is not None:
    if current.data==target:
        if previous is None:
            head=current.next
        else:
            previous.next=current.next
        break
    previous=current
    current=current.next
current=head
while current is not None:
    print(current.data,end="->")
    current=current.next
print("None")
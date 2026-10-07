class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def create_list(nums):
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
    return head
a = list(map(int, input("Enter List A: ").split()))
b = list(map(int, input("Enter List B: ").split()))
headA=create_list(a)
headB=create_list(b)
dummy=Node(0)
tail=dummy
while headA is not None and headB is not None:
    if headA.data<=headB.data:
        tail.next=headA
        headA=headA.next
    else:
        tail.next=headB
        headB=headB.next
    tail=tail.next
if headA is not None:
    tail.next=headA
else:
    tail.next=headB
current=dummy.next
while current is not None:
    print(current.data,end="->")
    current=current.next
print('None')
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res=ListNode(0)
        p=res
        carry_flag=0
        p1=l1
        p2=l2
        while p1.next is not None or p2.next is not None:
            if p1.next is None:
                p1.next=ListNode(0)
            if p2.next is None:
                p2.next=ListNode(0)
            p1=p1.next
            p2=p2.next
        while l1 is not None and l2 is not None:
            single_sum=l1.val+l2.val+carry_flag
            carry_flag=0
            if single_sum>9:
                carry_flag=1
                single_sum-=10
            temp=ListNode(single_sum)
            p.next=temp
            p=p.next
            l1=l1.next
            l2=l2.next
        if carry_flag==1:
            p.next=ListNode(1)
        return res.next
l1=ListNode(1)
l1.next=ListNode(8)
# l1.next.next=ListNode(3)
l2=ListNode(0)
# l2.next=ListNode(6)
# l2.next.next=ListNode(4)
s=Solution()
res=s.addTwoNumbers(l1,l2)
while res is not None:
    print(res.val)
    res=res.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ptr=head
        l=0
        while ptr!=None:
            l+=1
            ptr=ptr.next
        ptr=head
        target=l-n
        prev=head
        if target==0:
            head=head.next
            return head

        
        cnt=0
        while ptr!=None:
            if cnt==target:
                prev.next=ptr.next
                ptr.next=None
                return head
            cnt+=1
            prev=ptr
            ptr=ptr.next
            


        
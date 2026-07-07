# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        n = 0
        ptr = head

        while ptr:
            n += 1
            ptr = ptr.next

        index = {}

        ptr = head
        i = 0

        while ptr:
            index[i] = ptr
            ptr = ptr.next
            i += 1

        left = 0
        right = n - 1

        ptr = index[0]

        while left < right:
            ptr.next = index[right]
            ptr = ptr.next
            right -= 1

            if left == right:
                break

            left += 1
            ptr.next = index[left]
            ptr = ptr.next

        ptr.next = None
            
        


        
        
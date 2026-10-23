# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        ptrlist = []
        curr = head
        while curr:
            ptrlist.append(curr)
            curr = curr.next

        new = ListNode()
        ptr = new

        
        while ptrlist:
            
            forw = 0
            ptr.next = ptrlist[forw]
            ptrlist.pop(forw)
            ptr.next.next = None
            ptr = ptr.next

            
            if len(ptrlist) != 0:
                back = len(ptrlist)-1
                ptr.next = ptrlist[back]
                ptrlist.pop(back)
                ptr = ptr.next
                ptr.next = None
         
        
           
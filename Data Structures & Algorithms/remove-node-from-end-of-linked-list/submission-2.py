# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodelist = []
        
        adder = head
        while adder:
            nodelist.append(adder)
            adder = adder.next

        nodelist.pop((len(nodelist)-n))

        newnodes = ListNode()
        curr = newnodes
        for node in nodelist:
            curr.next = node
            curr = curr.next
        curr.next = None

        return newnodes.next
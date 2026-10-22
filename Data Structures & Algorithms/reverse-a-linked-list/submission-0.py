# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        curr = head
        while curr != None:
            arr.append(curr.val)
            curr = curr.next
        
        listlen = len(arr)
        
        curr = head
        for i in range(listlen-1, -1, -1):
            curr.val = arr[i]
            curr = curr.next

        return head
        
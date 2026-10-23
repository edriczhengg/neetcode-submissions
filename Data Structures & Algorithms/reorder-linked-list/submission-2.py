# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        list2 = slow.next
        slow.next = None

        prev = None
        while list2:
            temp = list2.next
            list2.next = prev
            prev = list2
            list2 = temp

        list1 = head
        list2 = prev
        while list1 and list2:
            temp1 = list1.next
            temp2 = list2.next
            list1.next = list2
            list1 = list1.next
            list1.next = temp1
            list1 = list1.next
            list2 = temp2


#       
# [1]->[2]->[3]->None. None<-[4]<-[5]<-[6]
#.      t1    S                    t/l2
# [1]->[2]->[3]->None. None<-[4]<-[5]
#       t2   S                    t/l2     
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode() # dummy head of our output list - useful to avoid condition where you inserting node in empty list, without a dummy node it will be tricky to solve this problem as to how to create the output list, and maintain a head pointer for it.
        p = dummy 
        
        while l1 and l2: # while both non None
            if l1.val < l2.val: # if l1 value is less, add that to p.next
                p.next = l1
                l1 = l1.next # move forward
            else:
                p.next = l2 # else add l2 for p.next
                l2 = l2.next # move forward
            p = p.next # always move this forward
        
        if l1:  # if l1 is not None yet, l1 was longer list
            p.next = l1 # make p.next point to remainder of l1
        else:
            p.next = l2 # else l2
        
        return dummy.next # return dummy.next as that is where our merged list started
            
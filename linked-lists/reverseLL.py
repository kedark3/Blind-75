# Approach using Stack.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        stack = list()
        p1 = head
        while p1:
            stack.append(p1)
            p1 = p1.next

        reverse = stack.pop()
        while stack:
            n = stack.pop()
            n.next.next = n

        head.next = None
        return reverse

# approach : using 3 pointers
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        if not head.next:
            return head
        
        p1 = None
        p2 = head
        p3 = head.next
        while p3:
            p2.next = p1
            p1 = p2
            p2 = p3
            p3 = p3.next
        p2.next = p1
        head = p2
        return p2

# Approach: Recursive

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reverse = self.helper(head)
        if head:
            head.next = None
        return reverse
        
        
        
    def helper(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        reverse = self.reverseList(head.next)

        head.next.next = head
        
        return reverse


# approach: recursive without helper

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        reverse = self.reverseList(head.next)

        head.next.next = head
        head.next = None
        return reverse
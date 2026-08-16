# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #we can use slow and fast pointers such that they have "n" nodes distance between them
        #since 1 <= n <= sz where sz is the number of nodes
        #we can then traverse through until we hit fast.next=None
        #here slow will be the node the node which needs to be removed so we track prev_slow
        #we then point prev_slow=slow.next
        dummy=ListNode(0,head)
        prev_slow = dummy
        slow,fast=head,head
        for i in range(n-1):
            fast=fast.next
        while fast and fast.next:
            prev_slow=slow
            slow=slow.next
            fast = fast.next
        prev_slow.next=slow.next
        return dummy.next
        

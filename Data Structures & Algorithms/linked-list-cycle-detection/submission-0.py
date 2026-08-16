# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head,head
        #when ur fast pointer is slower than ur slow pointer 
        #then the node at ur fast pointer is the index where the cycle starts
        while fast and fast.next: #but slow and fast will always exist since this is a cycle? 
            slow = slow.next
            fast = fast.next.next
            if fast==slow:#idk what went wrong here
                return True
        return False #this solution is only good for sorted lists where each element is unique
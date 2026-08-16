# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #we take the middle of the linkedlist and point it to None, giving us two lists: first and second
        #we reverse the second and then insert the nodes of the second in the first until there are no nodes in the second
        slow,fast=head,head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next#preserve the head of the second list
        slow.next = None#point the middle to nothing 
        #reverse the second list
        prev_second=None
        while second:
            next_node=second.next
            second.next = prev_second
            prev_second=second
            second=next_node
        second_head=prev_second
        #point the head of the second list and point it to first.next
        #now take the head of the first list point it to the head of the second list
        #then increement first like first=first.next.next until we run out of second list and second = second_next
        prev = None
        curr_first=head
        curr_second=second_head
        while curr_second:
            next_node_first=curr_first.next
            next_node_second=curr_second.next
            
            curr_second.next=next_node_first
            curr_first.next=curr_second

            curr_first = next_node_first
            curr_second = next_node_second
        return 


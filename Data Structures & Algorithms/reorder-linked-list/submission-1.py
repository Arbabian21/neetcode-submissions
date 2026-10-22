# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:        
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # now we have to reverse the second half of the linked list
        secondHalf = slow.next
        slow.next = None
        prev = None
        while secondHalf:
            temp = secondHalf.next
            secondHalf.next = prev
            prev = secondHalf
            secondHalf = temp
        
        # merge the two halves now
        secondHalf = prev # because by the end of the while loop above secondHalf ends up being None
        firstHalf = head

        while secondHalf:
            temp1, temp2 = firstHalf.next, secondHalf.next
            firstHalf.next = secondHalf
            secondHalf.next = temp1
            firstHalf = temp1
            secondHalf = temp2
                


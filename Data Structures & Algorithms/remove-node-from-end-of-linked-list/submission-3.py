# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummyNode = ListNode()
        dummyNode.next = head

        left, right = dummyNode, head

        for _ in range(n):
            right = right.next

        while right:
            left = left.next
            right = right.next

        left.next = left.next.next
        return dummyNode.next
        # slow, fast = head, head.next
        # counter = 1

        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next
        #     counter += 1
        
        # target = counter*2 -n
        # counter = 1
        # prev = None

        # while counter < target:
        #     prev = slow
        #     slow = slow.next
        #     counter += 1
        
        # if prev and slow.next:
        #     prev.next = slow.next
        
        # if head == slow:
        #     head = slow.next

        # slow.next = None
        # slow = None

        # return head
        

        

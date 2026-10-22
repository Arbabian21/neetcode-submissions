# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prevNode, current = None, head

        while current:
            if current.next == None:
                head = current
                current.next = prevNode
                break
            tempNode = current.next
            current.next = prevNode
            prevNode = current
            current = tempNode

        return head
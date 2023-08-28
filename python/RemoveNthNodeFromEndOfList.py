# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        pos_to_delete = 0
        current = head
        while current:
            current = current.next
            pos_to_delete += 1
        
        pos_to_delete -= n
        if pos_to_delete == 0:
            return head.next
        
        current = head
        curr_pos = 0
        while current:
            if curr_pos == pos_to_delete - 1:
                if current.next.next:
                    current.next = current.next.next
                else:
                    current.next = None
                break
            curr_pos += 1
            current = current.next

        return head

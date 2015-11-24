# Definition for singly-linked list
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        while cur:
            if cur.next is None:
                break
            elif cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head

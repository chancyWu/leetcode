class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        # if head is None or one list node in the head
        if head is None or head.next is None:
            return head
        
        temp = head.next
        head.next = None
        while temp is not None:
            temp2 = temp.next
            temp.next = head
            head = temp
            temp = temp2
        return head

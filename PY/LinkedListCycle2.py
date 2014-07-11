__author__ = 'zhengqin'


class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        if head == None: return None
        slow = head
        fast = head
        while fast != None and fast.next != None :
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return fast
        return None
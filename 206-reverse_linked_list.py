class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr:
            nextTemp = curr.next
            curr.next = prev
            prev = curr
            curr = nextTemp
        return prev
'''
Time complexity : O(n)
Space complexity : O(1)
'''
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        if not head or not head.next:
            return head
        
        p = self.reverseList(head.next)
        head.next.next = head 
        head.next = None
        return p
'''
Time complexity : O(n)
Space complexity : O(n) The extra space comes from implicit stack space due to recursion. 
The recursion could go up to nn levels deep.
'''
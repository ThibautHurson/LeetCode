# Approach 1: Reverse the 2nd half and compare
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        node = None

        # Reverse the 2nd half
        while slow:
            nxt = slow.next
            slow.next = node

            node = slow
            slow = nxt

        while node:
            if head.val != node.val:
                return False
            node = node.next
            head = head.next
        return True

'''
Time compexity: O(N) but two pass
Space complexity: O(1)
'''

# Approach 2: Reverse the first half then compare with the 2nd half
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        rev = None
        while fast and fast.next:
            fast = fast.next.next

            rev, rev.next, slow = slow, rev, slow.next
        
        if fast:
            slow = slow.next

        while rev:
            if slow.val != rev.val:
                return False
            rev = rev.next
            slow = slow.next
        return True

'''
Time compexity: O(N) one pass
Space complexity: O(1)
'''
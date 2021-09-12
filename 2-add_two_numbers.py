# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        root = ListNode()
        head = root
        counter = 0
        while l1 and l2:
            curr_sum = (l1.val + l2.val + counter)
            head.next = ListNode(curr_sum % 10)
            counter = curr_sum // 10
            
            l1, l2, head = l1.next, l2.next, head.next
            
        l = l1 or l2
        while l:
            curr_sum = (l.val + counter)
            head.next = ListNode(curr_sum % 10)
            counter = curr_sum // 10
            l, head = l.next, head.next
        if counter:
            head.next = ListNode(counter % 10) 
        return root.next
            
'''
Time complexity : O(max(m,n)). Assume that mm and nn represents the length of l1 and l2 respectively,
 the algorithm above iterates at most max(m,n) times.

Space complexity : O(max(m,n)). The length of the new list is at most max(m,n)+1.

**Follow up:
What if the the digits in the linked list are stored in non-reversed order? **
Solution:
We need to add numbers from the most right digit to left digit.
Compared with last question, we can reverse two lists and add them.
And reverse our output is correct answer.
'''  

# Even shorter
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        root = ListNode()
        head = root
        counter = 0
        while l1 or l2 or counter:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            curr_sum = (x + y + counter)
            head.next = ListNode(curr_sum % 10)
            counter = curr_sum // 10
            
            if l1: l1 = l1.next
            if l2: l2 = l2.next

            head = head.next

        return root.next  
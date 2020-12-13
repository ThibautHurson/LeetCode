# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        root = head = ListNode((l1.val + l2.val)%10)
        hold = (l1.val +l2.val)//10
        
        while l1.next and l2.next:
            
            head.next = ListNode((l1.next.val + l2.next.val + hold)%10)
            hold = (l1.next.val +l2.next.val + hold)//10

            l1 = l1.next
            l2 = l2.next
            head = head.next
        
        if l1.next:
            while l1.next:
                head.next = ListNode((l1.next.val + hold)%10)
                hold = (l1.next.val + hold)//10
                l1 = l1.next
                head = head.next

        else:
             while l2.next:
                head.next = ListNode((l2.next.val + hold)%10)
                hold = (l2.next.val + hold)//10            
                l2 = l2.next
                head = head.next
        if hold!=0:
            head.next = ListNode(hold%10)
        
        
        return root
            
'''
Time complexity : O(max(m,n)). Assume that mm and nn represents the length of l1l1 and l2l2 respectively, the algorithm above iterates at most \max(m, n)max(m,n) times.

Space complexity : O(max(m,n)). The length of the new list is at most \max(m,n) + 1max(m,n)+1.

**Follow up:
What if the the digits in the linked list are stored in non-reversed order? **
Solution:
We need to add numbers from the most right digit to left digit.
Compared with last question, we can reverse two lists and add them.
And reverse our output is correct answer.
'''  
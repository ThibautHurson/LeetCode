# Approach 1: Naive Pass in A than B with a memory
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        memoA = set()
        while headA:
            memoA.add(headA)
            headA = headA.next
        while headB:
            if headB in memoA:
                return headB
            headB = headB.next

        return None
'''
Time complexity: 0(length A + length B)
Space complexity: 0(length A)
'''

# Approach 2: 0(1) memory
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        a, b = headA, headB
        while (a != b):
            a = headB if not a else a.next
            b = headA if not b else b.next
        return a
'''
Time complexity: 0(max(length A, length B))
Space complexity: 0(1)
'''
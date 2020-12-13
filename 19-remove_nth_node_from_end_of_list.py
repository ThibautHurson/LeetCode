class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:      
        root = prev = head
        if not head.next:
            return None  
        
        for i in range(n):
            head = head.next

        if not head: #have to rm the first element
            return root.next
        
        while head.next:
            head = head.next
            prev = prev.next
           
        prev.next = prev.next.next
        return root

'''
Time complexity : O(L). The algorithm makes one traversal of the list of L nodes.
Space complexity : O(1).
'''

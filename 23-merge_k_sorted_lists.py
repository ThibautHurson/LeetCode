#Approach 1: Brute Force

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        self.nodes = []
        root = head = ListNode(0)
        for l in lists:
            while l:
                self.nodes.append(l.val)
                l = l.next
        
        for val in sorted(self.nodes):
            head.next = ListNode(val)
            head = head.next
        return root.next
'''
Time complexity : O(NlogN) where NN is the total number of nodes.

Collecting all the values costs O(N) time.
A stable sorting algorithm costs O(NlogN) time.
Iterating for creating the linked list costs O(N) time.
Space complexity : O(N).

Sorting cost O(N) space (depends on the algorithm you choose).
Creating a new linked list costs O(N) space.
'''
#Approach 2: Merge with Divide And Conquer

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        amount = len(lists)
        interval = 1
        while interval < amount:
            for i in range(0, amount-interval, interval * 2):
                lists[i] = self.merge2Lists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0] if amount > 0 else None

    def merge2Lists(self, l1, l2):
        head = point = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                point.next = l1
                l1 = l1.next
            else:
                point.next = l2
                l2 = l2.next
            point = point.next
        if not l1:
            point.next=l2
        else:
            point.next=l1
        return head.next
'''
Time complexity : O(Nlogk) where k is the number of linked lists.

We can merge two sorted linked list in O(n) time where nn is the total number of nodes in two lists.
Sum up the merge process and we can get: 
​	
Space complexity : O(1) je pense que c'est faux
'''
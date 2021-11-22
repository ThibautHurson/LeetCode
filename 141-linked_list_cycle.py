# Turtoise and hare kind of problem
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False

'''
Time complexity: O(N)
Space complexity: O(1)


If the list has N nodes, then in <= N steps, either the fast pointer will find the end of the list, 
or there is a loop and the slow pointer will be in the loop.

Lets say the loop is of length M <= N: Once the slow pointer is in the loop, both the fast and slow 
pointers will be stuck in the loop forever. Each step, the distance between the fast and the slow 
pointers will increase by 1. When the distance is divisible by M, then the fast and slow pointers 
will be on the same node and the algorithm terminates. The distance will reach a number divisible 
by M in <= M steps.

So, getting the slow pointer to the loop, and then getting the fast and slow pointers to meet 
takes <= N + M <= 2N steps, and that is in O(N)

In fact, you can get a tighter bound on the step count if you note that when there's a loop, the slow 
pointer will get to it in N - M steps, so the total step count is <= N.
'''

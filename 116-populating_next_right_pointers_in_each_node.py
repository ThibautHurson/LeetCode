# Approach 1: BFS
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        queue = collections.deque()
        queue.append((1, root))
        
        while queue:
            depth, head = queue.popleft()
            if queue:
                head.next =  queue[0][1] if queue[0][0] == depth else None
            else:
                head.next = None
                    
            if head.left:
                queue.append((depth + 1, head.left))
            if head.right:
                queue.append((depth + 1, head.right))
            
        return root
'''
Time complexity: 
O(|V|+|E|) = O(b**d)
Space complexity: O(|V|+|E|) = O(b**d)

with |V| the number of vertex, |E| the number of edges
with b the branching factor and d the depth
'''

# Approach 2: Next Pointer
class Solution:
    def connect(self, root):
        if not root:
            return root
        head = root
        left = head.left

        while head.left:
            head.left.next = head.right
            if head.next:
                head.right.next = head.next.left
                head = head.next
            else:
                head = left
                left = head.left
        return root

'''
Time complexity: 
O(|V|+|E|)
Space complexity: O(1)
'''

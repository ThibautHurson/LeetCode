# Note: Number of subsets: 2^N, since each element could be absent or present.

# Approach 1: Cascading
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            res += [curr + [num] for curr in res]
        return res
'''
Let's start from empty subset in output list. At each step one takes new integer 
into consideration and generates new subsets from the existing ones.

Time complexity: O(N * 2^N) to generate all subsets and then copy them into output list. --> 2 for loops
Space complexity: O(N * 2^N) This is exactly the number of solutions for subsets multiplied. --> 2 for loops 
by the number N of elements to keep for each subset.
'''

# Approach 2: Backtracking
''' 
Idea: Power set is all possible combinations of all possible lengths, from 0 to n.
Given the definition, the problem can also be interpreted as finding the power set from a sequence.

So, this time let us loop over the length of combination, rather than the candidate numbers, and generate all combinations for a given length with the help of backtracking technique.
'''


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first = 0, curr = []):
            if len(curr) == k:
                res.append(curr[:])
                return
            for i in range(first, n):
                curr.append(nums[i])
                backtrack(i+1, curr)
                curr.pop()

        res = []
        n = len(nums)
        for k in range(n + 1):
            backtrack()
        return res

'''
Time complexity: O(N×2**N) to generate all subsets and then copy them into output list.

Space complexity: O(N). We are using O(N) space to maintain curr, and are modifying curr in-place 
with backtracking. Note that for space complexity analysis, we do not count space that is only used 
for the purpose of returning output, so the output array is ignored.
'''


# Approach 3: Lexicographic (Binary Sorted) Subsets
'''
The idea is that we map each subset to a bitmask of length n, where 1 on the ith position in bitmask 
means the presence of nums[i] in the subset, and 0 means its absence.
'''
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        output = []
        
        for i in range(2**n, 2**(n + 1)):
            # generate bitmask, from 0..00 to 1..11
            bitmask = bin(i)[3:]
            
            # append subset corresponding to that bitmask
            output.append([nums[j] for j in range(n) if bitmask[j] == '1'])
        
        return output

'''
Time complexity: O(N×2**N) to generate all subsets and then copy them into output list.

Space complexity: O(N×2**N) to keep all the subsets of length NN, since each of NN elements could 
be present or absent.
'''
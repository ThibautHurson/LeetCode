class Solution:
    def permute(self, nums):
        def backtrack(start, end):
            if start == end:
                ans.append(nums[:])
            for i in range(start, end):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start+1, end)
                nums[start], nums[i] = nums[i], nums[start]
                
        ans = []
        backtrack(0, len(nums))
        return ans

'''
Slicing:
This is the easiest and the fastest way to clone a list. This method is considered when 
we want to modify a list and also keep a copy of the original. In this we make a copy of 
the list itself, along with the reference. This process is also called cloning. This 
technique takes about 0.039 seconds and is the fastest technique.
If we had written nums insteed of nums[:], then, every element in ans would have pointed to nums
and thus to its current state. As a consequence, every element in ans would have been 
modified as often as nums.

Example:
>>> original = [1, 2, 3]
>>> other = original
>>> original[:] = [0, 0] # changes the contents of the list that both
                         # original and other refer to 
>>> other # see below, now you can see the change through other
[0, 0]

>>> original = [1, 2, 3]
>>> other = original
>>> original = [0, 0] # original now refers to a different list than other
>>> other # other remains the same
[1, 2, 3]
'''
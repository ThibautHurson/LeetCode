
# Approach: Sorting
# we sort the intervals by their start value
class Solution:
    def merge(self, intervals):
        intervals.sort() #SORTING IS DONE INPLACE!!!
        res = []
        current_min, current_max = intervals[0][0], intervals[0][1]
        for i in range(1,len(intervals)):
            if intervals[i][0] <= current_max and intervals[i][1] > current_max:
                current_max = intervals[i][1]
            if intervals[i][0] > current_max:
                res.append([current_min, current_max])
                current_min, current_max = intervals[i][0], intervals[i][1]
        res.append([current_min, current_max])

        return res

intervals = [[1,4],[4,5]]
sol = Solution()
print(sol.merge(intervals))


'''
Time complexity : O(nlogn)
Space complexity : O(logN) (or O(n))
    If we can sort intervals in place, we do not need more than constant additional space, 
    although the sorting itself takes O(logn) space. Otherwise, we must allocate linear space 
    to store a copy of intervals and sort that.
'''
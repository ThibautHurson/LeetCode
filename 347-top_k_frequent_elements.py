from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        counter = counter.most_common(k)
        return [counter[i][0] for i in range(k)]

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]: 
        # O(1) time 
        if k == len(nums):
            return nums
        
        # 1. build hash map : character and how often it appears
        # O(N) time
        count = Counter(nums)   
        # 2-3. build heap of top k frequent elements and
        # convert it into an output array
        # O(N log k) time
        return heapq.nlargest(k, count.keys(), key=count.get) 

'''Les 2 méthodes se valent
Time complexity : O(Nlogk) if k < Nk<N and O(N) in the particular case of N = kN=k. That ensures time complexity to be better than \mathcal{O}(N \log N)O(NlogN).

Space complexity : O(N+k) to store the hash map with not more NN elements and a heap with kk elements.
'''

#Approach with defaultdict and sort
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return [strs]
        
        res = defaultdict(list)
        for s in strs:
            res["".join(sorted(s))].append(s)  #tuple(sorted(s)) works too
        return res.values()
'''N is the length of strs, and k the maximum length f a string in strs
Time complexity: O(N*k*log(k)) sort N times k elements (sort takes klog(k))
Spacce complexity: O(Nk) total number of information stored in res
'''
#Approach 2: Categorize by Count
#abbccc will be (1, 2, 3, 0, 0, ..., 0), where there are 26 entries total.
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return [strs]
        
        res = collections.defaultdict(list)
        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c) - ord('a')] +=1
            res[tuple(count)].append(s)
        return res.values()
'''
Time complexity: O(Nk) Counting each string is linear in the size of the string, and we count every string
Space Complexity: O(Nk) the total information content stored in ans.
'''
                
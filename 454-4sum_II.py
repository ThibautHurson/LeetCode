#Methode 1
class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:

        hashtable = {}
        for a in A:
            for b in B :
                if a + b in hashtable :
                    hashtable[a+b] += 1
                else :
                    hashtable[a+b] = 1
        count = 0         
        for c in C :
            for d in D :
                if -c - d in hashtable :
                    count += hashtable[-c-d]
        return count
'''
Time: O(n^2)
Space: O(n) dans le pire des cas je pense
'''
#Methode 2
def fourSumCount(self, A, B, C, D):
    AB = collections.Counter(a+b for a in A for b in B)
    return sum(AB[-c-d] for c in C for d in D)
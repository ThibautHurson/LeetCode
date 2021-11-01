# DFS with Backtracking
class Solution:
    def partition(self, s):
        result = []
        curr_list = []
        self.dfs(result, s, 0, curr_list)
        return result

    def dfs(self, result, s, start, curr_list):
        if start >= len(s):
            result.append(curr_list[:]) # Need to copy curr_list as lists are mutable
        for end in range(start, len(s)):
            if self.isPalindrome(s, start, end):
                curr_list.append(s[start: end + 1])
                self.dfs(result, s, end + 1, curr_list)

                # backtrack and remove the current substring from curr_list
                curr_list.pop()

    def isPalindrome(self, s, low, high):
        while low < high:
            if s[low] != s[high]:
                return False
            high -= 1
            low += 1
        return True

'''
Time complexity: O(N * 2**N), where N is the length of the string.

For each character in the string we have 2 choices to create new palindrom 
substrings, one is to join with previous substring (for(...end++)) and another 
is to start a new palindrom substring (dfs(..end+1..)). Thus in the worst case 
there are 2^N palindrom substrings. Each substring will take O(N) time to 
check if it's palindrom and O(N) time to generate substring from start to end 
indexes.

In total we have O(2^N * (N + N)) = O(2^N * 2N) = O(N*2^N)


Space complexity: O(N), where N is the length of the string ss. This space 
will be used to store the recursion stack. 
For s = aaa, the maximum depth of the recursive call stack is 3 which is 
equivalent to N.
'''


# Dynamic Programming with Backtracking
'''
A given string ss starting at index start and ending at index end is a 
palindrome if following conditions are satisfied :

The characters at start and end indexes are equal.
The substring starting at index start+1 and ending at index end−1 is a 
palindrome.


Let NN be the length of the string. To determine if a substring starting at 
index start and ending at index end is a palindrome or not, we use a 2 
Dimensional array dp of size N*N where,

dp[start][end] = true, if the substring beginning at index start and ending 
at index end is a palindrome.

Otherwise, dp[start][end] == false.

Also, we must update the dp array, if we find that the current string is a 
palindrome.
'''
class Solution2:
    def partition(self, s):
        dp = [[None for _ in range(len(s))] for _ in range(len(s))]
        result = []
        curr_list = []
        self.dfs(result, s, 0, curr_list, dp)
        return result

    def dfs(self, result, s, start, curr_list, dp):
        if start >= len(s):
            result.append(curr_list[:])

        for end in range(start, len(s)):
            if s[start] == s[end] and (end - start <= 2 or dp[start + 1][end - 1]):
                dp[start][end] = True
                curr_list.append(s[start: end + 1])

                self.dfs(result, s , end + 1, curr_list, dp)

                # backtrack
                curr_list.pop()

'''
Time complexity: O(N * 2**N) same as in approach 1, but we are eliminating 
one additional iteration to check if substring is a palindrome or not.

Space Complexity: O(N⋅N), where NN is the length of 
the string s. The recursive call stack would require N space as in 
Approach 1. Additionally we also use 2 dimensional array dp of size N⋅N .
'''
s = "aab"
sol = Solution2()
print(sol.partition(s))




from string import ascii_letters

class Solution:
	def titleToNumber(self, columnTitle: str) -> int:
		letters = ascii_letters[26:]
		mapping = dict(zip(letters, list(range(1, 27))))

		res = 0
		for k in range(len(columnTitle) - 1, -1, -1):
			res += (26**(len(columnTitle) -1 - k))*mapping[columnTitle[k]]
		return res

'''
Time complexity : O(N)

Space complexity : O(1)
'''
# Same approach but using ord() function
class Solution:
	def titleToNumber(self, columnTitle: str) -> int:
		res = 0
		for k in range(len(columnTitle) - 1, -1, -1):
			res += (26**(len(columnTitle) -1 - k))*(ord(columnTitle[k]) - ord('A') +1)
		return res

name = "FXSHRXW"
sol = Solution()
print(sol.titleToNumber(name))


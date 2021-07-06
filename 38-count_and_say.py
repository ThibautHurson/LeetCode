import itertools
# Approach 1
class Solution:
    def countAndSay(self, n: int) -> str:
        last = "1"
        for k in range(n-1):
            count, current_char, new = 1, last[0], ""
            for i in range(1,len(last)):
                if last[i] == current_char:
                    count += 1
                else:
                    new += str(count) + current_char
                    current_char, count = last[i], 1

            last = new + str(count) + current_char
            
        return last

# Approach 2: Using groupby
class Solution2:
    def countAndSay(self, n: int) -> str:
        s = "1"
        for k in range(n-1):
            s = ''.join(str(len(list(group))) + digit for digit, group in itertools.groupby(s))
        return s

sol = Solution2()
print(sol.countAndSay(4))
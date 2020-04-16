# Intuition:
# One pass on the string S,
# we need to know,
# how many ')' we are waiting for.

# If we meet too many ')', we can return false directly.
# If we wait for no ')' at the end, then we are good.


# Explanation:
# We count the number of ')' we are waiting for,
# and it's equal to the number of open parenthesis.
# This number will be in a range and we count it as [cmin, cmax]

# cmax counts the maximum open parenthesis,
# which means the maximum number of unbalanced '(' that COULD be paired.
# cmin counts the minimum open parenthesis,
# which means the number of unbalanced '(' that MUST be paired.


# Example:
# It's quite straight forward actually.
# When you met "(", you know you need one only one ")", cmin = 1 and cmax = 1.
# When you met "(*(", you know you need one/two/three ")", cmin = 1 and cmax = 3.

# The string is valid for 2 condition:

# cmax will never be negative.
# cmin is 0 at the end.

# Time Complexity:
# One pass O(N) time, Space O(1)


class Solution(object):
    def checkValidString(self, s):
        cmin = cmax = 0
        for i in s:
            if i == '(':
                cmax += 1
                cmin += 1
            if i == ')':
                cmax -= 1
                cmin = max(cmin - 1, 0)
            if i == '*':
                cmax += 1
                cmin = max(cmin - 1, 0)
            if cmax < 0:
                return False
        return cmin == 0


s= Solution()
print(s.checkValidString("(*()"))
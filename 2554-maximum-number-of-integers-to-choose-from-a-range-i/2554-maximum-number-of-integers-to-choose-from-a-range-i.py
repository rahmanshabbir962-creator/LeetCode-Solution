class Solution(object):
    def maxCount(self, banned, n, maxSum):
        banned = set(banned)
        total = 0
        count = 0

        for i in range(1, n + 1):
            if i not in banned and total + i <= maxSum:
                total += i
                count += 1

        return count
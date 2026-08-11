class Solution(object):
    def separateDigits(self, nums):
        result = []

        for i in nums:
            for digits in str(i):
                result.append(int(digits))

        return result
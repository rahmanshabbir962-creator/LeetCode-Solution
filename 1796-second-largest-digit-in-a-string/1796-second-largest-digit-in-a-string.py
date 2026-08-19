class Solution:
    def secondHighest(self, s):
        digits = set()

        for ch in s:
            if ch.isdigit():
                digits.add(int(ch))

        digits = sorted(digits)

        if len(digits) < 2:
            return -1

        return digits[-2]
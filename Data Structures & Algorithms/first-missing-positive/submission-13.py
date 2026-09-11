class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        if not nums:
            return 1

        nums.sort()

        num = []

        # Keep only positive numbers and remove duplicates
        for x in nums:
            if x > 0 and x not in num:
                num.append(x)

        # No positive numbers
        if not num:
            return 1

        # 1 is missing
        if num[0] != 1:
            return 1

        # Find the first gap
        for i in range(len(num) - 1):
            if num[i + 1] != num[i] + 1:
                return num[i] + 1

        # All numbers are consecutive
        return num[-1] + 1
class Solution(object):
    def zeroFilledSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0  # Tracks consecutive zeros
        result = 0  # Stores total number of zero-filled subarrays

        for num in nums:
            if num == 0:
                count += 1
                result += count
            else:
                count = 0  # Reset count when a non-zero is found

        return result

sol = Solution()
print(sol.zeroFilledSubarray([1, 3, 0, 0, 2, 0, 0, 4]))  # Output: 6
print(sol.zeroFilledSubarray([0, 0, 0, 2, 0, 0]))
print(sol.zeroFilledSubarray([2, 10, 2019]))
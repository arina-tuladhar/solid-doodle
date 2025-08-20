class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0          # pointer for the next position to place a non-val element
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k+=1

        return k

sol = Solution()

nums = [3, 2, 2, 3]
val = 3

k = sol.removeElement(nums, val)

print("k =", k)
print("Modified nums (first k elements):", nums[:k])

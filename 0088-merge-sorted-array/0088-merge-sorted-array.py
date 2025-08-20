class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None. Do not return anything, modify nums1 in-place instead.
        """
        # Start from the end of nums1 and nums2
        p1 = m - 1  # Pointer for end of valid elements in nums1
        p2 = n - 1  # Pointer for end of nums2
        p = m + n - 1  # Pointer for end of merged array in nums1

        # Merge nums1 and nums2 from the back
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        # If there are leftover elements in nums2, copy them
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1

nums1 = [1]
m = 1
nums2 = []
n = 0

merge(nums1, m, nums2, n)
print(nums1)      
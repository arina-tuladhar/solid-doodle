class Solution(object):
    def judgePoint24(self, cards):
        """
        :type cards: List[int]
        :rtype: bool
        """
        def helper(nums):
            if len(nums) == 1:
                return abs(nums[0] - 24) < 1e-6
            
            for i in range(len(nums)):
                for j in range(len(nums)):
                    if i != j:
                        a, b = nums[i], nums[j]
                        next_nums = [nums[k] for k in range(len(nums)) if k != i and k != j]

                        results = [a + b, a - b, b - a, a * b]
                        if abs(b) > 1e-6:
                            results.append(a / float(b))
                        if abs(a) > 1e-6:
                            results.append(b / float(a))
                        
                        for res in results:
                            if helper(next_nums + [res]):
                                return True
            return False

        for perm in itertools.permutations(cards):
            if helper(list(perm)):
                return True
        return False
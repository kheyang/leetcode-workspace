from typing import List
import time
class Solution:
    def twoSumSlow(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if target - nums[i] == nums[j]:
                    return [i, j]

    def twoSumFast(self, nums: List[int], target: int) -> List[int]:
        refTab = {}
        for i in range(len(nums)):
            contra = target - nums[i]
            if contra not in refTab:
                refTab[nums[i]] = i
            else:
                return [refTab[contra], i]

solution = Solution()

print(solution.twoSumSlow([1,3,5,7,9], 8))
print(solution.twoSumSlow([5,5,5,5], 10))
print(solution.twoSumSlow([-1,-3,-5,-5], -6))
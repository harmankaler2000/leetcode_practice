class Solution:
    def triangleType(self, nums: List[int]) -> str:
        if len(nums) != 3:
            return "none"
        if len(set(nums)) == 1:
            return "equilateral"
        total_sum = sum(nums)
        for i in nums:
            if total_sum - i <= i:
                return "none"
        if len(set(nums)) == 2:
            return "isosceles"
        return "scalene"

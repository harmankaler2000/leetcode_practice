class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # brute force method
        for i in range(len(nums)):
            nums[i] = nums[i] * nums[i]
        nums.sort()
        return nums

class Solution:
    def maxAscendingSum(self, nums):
        max_sum = 0
        curr_sum = nums[0]
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                curr_sum += nums[i + 1]
            else:
                if curr_sum > max_sum:
                    max_sum = curr_sum
                curr_sum = nums[i + 1]
        if max_sum < curr_sum:
            max_sum = curr_sum
        return max_sum

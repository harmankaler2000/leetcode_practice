class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for index in range(len(nums)):
            second = (target - nums[index])
            if second in nums:
                sec_index = nums.index(second)
                if sec_index != index:
                    return [index, sec_index]

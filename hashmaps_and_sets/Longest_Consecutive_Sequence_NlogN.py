class Solution:
    def longestConsecutive(self, nums):
        if len(nums) < 1:
            return 0
        # delete duplicates as they don't matter
        nums = list(set(nums))
        # sort the array - O(NlogN)
        nums.sort()
        # go through the array and check the max seq
        max_seq = 1
        seq = 1
        for i in range(len(nums) - 1):
            if nums[i] + 1 == nums[i + 1]:
                seq += 1
            else:
                if max_seq < seq:
                    max_seq = seq
                seq = 1
        if max_seq < seq:
            max_seq = seq
        return max_seq

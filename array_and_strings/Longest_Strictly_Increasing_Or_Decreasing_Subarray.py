class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        # check longest increasing subarray
        # min length will be one
        inc_count = 1
        curr_index = 1
        # skip first index
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                curr_index += 1
            else:
                if inc_count < curr_index:
                    inc_count = curr_index
                curr_index = 1
        if curr_index > inc_count:
            inc_count = curr_index

        # calculate the dec now
        dec_count = 1
        curr_index = 1
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                curr_index += 1
            else:
                if dec_count < curr_index:
                    dec_count = curr_index
                curr_index = 1
        if curr_index > dec_count:
            dec_count = curr_index
        return max(inc_count, dec_count)

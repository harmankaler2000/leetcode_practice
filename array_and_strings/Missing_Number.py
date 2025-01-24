class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #loop over list to find the numbers missing
        length = len(nums)
        for number in nums:
            if number + 1 not in nums and number + 1 <= length:
                return number + 1
            elif number - 1 not in nums and number - 1 >= 0:
                return number - 1

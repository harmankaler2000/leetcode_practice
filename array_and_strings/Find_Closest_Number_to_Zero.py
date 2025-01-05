class Solution(object):
    def findClosestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        closest = nums[0]
        for element in nums:
            if abs(element) < abs(closest):
                closest = element
        if closest < 0 and abs(closest) in nums:
            return abs(closest)
        return closest

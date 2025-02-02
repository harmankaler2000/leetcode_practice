class Solution:
    def check(self, nums: List[int]) -> bool:
        if len(nums) == 2:
            return True
        turn = 0
        turn_index = 0
        for i in range(len(nums) - 1):
            if turn > 1:
                return False
            if nums[i] > nums[i + 1]:
                turn_index = i + 1
                turn += 1
        if turn == 0:
            return True

        # make sure that elements after the turn are in descending
        for i in range(turn_index, len(nums) - 1):
            if nums[i] > nums[i + 1]:
                return False
            
        if turn_index == len(nums) - 1 and nums[0] != nums[turn_index]:
            for i in range(len(nums) - 2):
                if nums[i] > nums[i + 1]:
                    return False
        # # make sure that the first element is larger or equal to the first element if turn index != 0
        if turn_index != 0 and nums[0] < nums[-1]:
            return False
        return True

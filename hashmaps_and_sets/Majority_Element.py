# makes use of Boyer-Moore's majority voting Alogirthm
# validation step is not added here as the question mentiones that we will always have a majority
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans = -1
        count = 0
        for num in nums:
            if count == 0:
                ans = num
                count = 1
            else:
                if num == ans:
                    count += 1
                else:
                    count -= 1
        return ans

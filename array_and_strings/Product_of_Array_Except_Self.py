class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        l_mul = 1
        r_mul = 1
        length = len(nums)
        l_arr = [1] * length
        r_arr = [1] * length
        for i in range(length):
            # opposite index from right
            j = - i - 1
            l_arr[i] = l_mul
            l_mul *= nums[i]
            r_arr[j] = r_mul
            r_mul *= nums[j]
        
        # final_output
        for index in range(length):
            ans.append(l_arr[index] * r_arr[index])
        return ans

class Solution:
    def smallerNumbersThanCurrent(self, nums):
        sorted_list = sorted(nums)
        dict = {}
        response = []
        for index in range(len(sorted_list)):
            actual_number = sorted_list[index]
            if actual_number not in dict.keys():
                dict[actual_number] = index
        for num in nums:
            response.append(dict[num])
        return response

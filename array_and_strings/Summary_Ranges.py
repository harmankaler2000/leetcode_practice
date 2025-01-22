class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not len(nums):
            return nums
        output_list = []
        range_list = [nums[0]]
        for index in range(1, len(nums)):
            if nums[index] == nums[index - 1] + 1:
                range_list.append(nums[index])
                print(range_list)
            else:
                if len(range_list) > 1:
                    output_list.append(f"{range_list[0]}->{range_list[len(range_list) - 1]}")
                else:
                    output_list.append(f"{range_list[0]}")
                range_list = [nums[index]]

        if len(range_list) > 1:
            output_list.append(f"{range_list[0]}->{range_list[len(range_list) - 1]}")
        else:
            output_list.append(f"{range_list[0]}")

        return output_list

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # find the distinct number of elements and create a dict with it and set count to 0
        count_dict = {}
        for element in set(nums):
            count_dict[element] = 0
        
        # loop over initial nums and update above counter
        for number in nums:
            count_dict[number] += 1

        # sort the dictionary by value
        updated_dict = dict(sorted(count_dict.items(), key=lambda item: item[1], reverse=True))

        # loop over the dictionary till the top k elements are selected
        index = 1
        response = []
        for key in updated_dict.keys():
            print("key: ", key)
            if index > k:
                break
            response.append(key)
            index += 1
        return response

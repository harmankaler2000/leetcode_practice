class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        product_dict = {}
        count = 0
        for i in range(len(nums)):
            # do not consider the previously checked values
            for j in range(i + 1, len(nums)):
                product = nums[i] * nums[j]
                if product not in product_dict.keys():
                    product_dict[nums[i] * nums[j]] = 1
                else:
                    product_dict[nums[i] * nums[j]] += 1
        
        # if a product occurs more than once only then consider
        # permutation formula is - 4 * (n) * (n-1)
        # if something occurs once if will not be considered acc to above
        for value in product_dict.values():
            count += 4 * value * (value - 1)
        return count

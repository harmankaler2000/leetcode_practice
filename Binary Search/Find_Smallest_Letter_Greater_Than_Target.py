class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        left = 0
        right = len(letters) - 1
        return_value = letters[0]
        while left <= right:
            mid = left + (right - left) // 2
            if ord(letters[mid]) > ord(target):
                return_value = letters[mid]
                right = mid - 1
            else:
                left = mid + 1
        return return_value
            

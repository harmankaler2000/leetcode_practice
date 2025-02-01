class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if the sets don't match simply return false
        if set(s) != set(t):
            return False
        # check if the count of each of the letter matches else false
        for letter in set(s):
            if s.count(letter) != t.count(letter):
                return False
        return True

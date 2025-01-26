class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # create a mapping of the letters in magazine
        # map for ransom note
        for letter in set(ransomNote):
            if letter not in magazine:
                return False
            if ransomNote.count(letter) > magazine.count(letter):
                return False
        return True

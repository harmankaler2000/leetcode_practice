class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # create a mapping of the letters in magazine
        map_mag = {}
        for letter in set(magazine):
            map_mag[letter] = magazine.count(letter)
        
        # map for ransom note
        for letter in set(ransomNote):
            if letter not in map_mag.keys():
                return False
            if ransomNote.count(letter) > map_mag[letter]:
                return False
        return True

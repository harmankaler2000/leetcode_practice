class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        for i in set(s1):
            if i not in s2:
                return False
            if s1.count(i) != s2.count(i):
                return False
        # check if we need to swap more than one element
        mismatch_count = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                mismatch_count += 1
        if mismatch_count not in [0, 2]:
            return False
        return True

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) > len(t):
            return False
        if s in t:
            return True
        final_list = ""
        index_s = 0
        # loop over t
        for index_t in range(len(t)):
            if len(final_list) == len(s):
                break
            if t[index_t] == s[index_s]:
                final_list += t[index_t]
                index_s += 1
        print(final_list)
        if s == final_list:
            return True
        return False
        

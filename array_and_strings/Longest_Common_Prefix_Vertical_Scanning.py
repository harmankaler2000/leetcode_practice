class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        min_length = float("inf")
        for s in strs:
            if len(s) < min_length:
                min_length = len(s)
        
        i = 0
        # iterate over all strs till the letter is common
        # this is vertical scanning
        while i < min_length:
            for s in strs:
                # check the index of each list compared to the first value
                if s[i] != strs[0][i]:
                    # return the list till that particular index
                    return s[:i]
            i += 1
        # return the strs first string till the ith index
        return strs[0][:i]

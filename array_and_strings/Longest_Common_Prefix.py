class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        common_string = strs[0]
        for index in range(1, len(strs)):
            # compare the common string with the current string and update the common
            common = ""
            for l_index in range(len(strs[index])) if len(strs[index]) < len(common_string) else range(len(common_string)):
                if common_string[l_index] == strs[index][l_index]:
                    common += common_string[l_index]
                else:
                    break
            # if common string is "" - break and return
            if common == "":
                return ""
            common_string = common
        return common_string

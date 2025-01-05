class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        if not word1 and not word2:
            return None
        if not word1:
            return word2
        if not word2:
            return word1

        diff = abs(len(word1) - len(word2))
        final_word = ""
        #loop over word1
        for index in range(len(word1)):
            #append the index position of word1 and word2
            final_word += word1[index]
            if index < len(word2):
                # the index is present in word2
                final_word += word2[index]
        if len(word2) > len(word1):
            final_word += word2[len(word1):len(word2)]
        return final_word

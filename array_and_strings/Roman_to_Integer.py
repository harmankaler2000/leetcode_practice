class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        final_number = 0
        roman_int_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900
        }
        # parse over the input roman numeral
        skip_index = None
        for index in range(len(s)):
            if index == skip_index:
                continue
            if s[index] in ("I", "X", "C") and index < len(s) - 1:
                # check if we need to substract a value
                if s[index] + s[index + 1] in roman_int_dict:
                    final_number += roman_int_dict[s[index] + s[index + 1]]
                    skip_index = index + 1
                    continue
            final_number += roman_int_dict[s[index]]
        return final_number

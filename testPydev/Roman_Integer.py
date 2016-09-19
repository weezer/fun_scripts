class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        roman_dict = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40,
                      'L': 50, 'XC': 90, 'C': 100, 'CD': 400, 'D': 500, 'CM': 900, 'M': 1000}

        prev = s[0]
        result = 0
        for i in s:
            if roman_dict[prev] < roman_dict[i]:
                result -= (2 * roman_dict[prev])
            result += roman_dict[i]
            prev = i

        return result

if __name__ == "__main__":
    s = Solution()
    print s.romanToInt("MCMXCVI")
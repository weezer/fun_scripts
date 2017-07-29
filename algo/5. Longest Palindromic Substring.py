class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        len_s = len(s)
        if len_s <= 1:
            return s
        str_matrix = [[0 for i in range(len_s)] for j in range(len_s)]
        for i in range(len_s):
            str_matrix[i][i] = True
            str_matrix[i][i-1] = True
        str_matrix[0][i] = 0
        max_len = 1
        rtr_answer = s[0]
        for i in range(1, len_s):
            for j in range(i, 0, -1):
                if str_matrix[j][i-1] and s[j-1] == s[i]:
                    str_matrix[j-1][i] = True
                    if i-j+2 >= max_len:
                        rtr_answer = s[j-1:i+1]
                        print rtr_answer
                        max_len = i-j+2
        return rtr_answer


if __name__ == "__main__":
    s = Solution()
    print s.longestPalindrome("abcaa")
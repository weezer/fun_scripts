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

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        len_s = len(s)
        if len_s <= 1:
            return len_s
        matrix_s = [[0 for i in range(len_s)] for i in range(len_s)]
        max_num = 0
        r_answer = s[0]
        for i in range(len_s):
            for j in range(i, -1, -1):
                if i == j:
                    matrix_s[i][j] = 1
                    continue
                if s[i] == s[j] and (matrix_s[i-1][j+1] != 0 or matrix_s[i][j+1] != 0):
                    matrix_s[i][j] = matrix_s[i-1][j+1] + 2
                    if max_num < matrix_s[i][j]:
                        max_num = matrix_s[i][j]
                        r_answer = s[j:j+max_num]
        print matrix_s
        return r_answer

if __name__ == "__main__":
    s = Solution()
    print s.longestPalindrome("cbbd")
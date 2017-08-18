class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        s_len = len(s)
        p_len = len(p)
        result_matrix  = [[False] * (s_len+1) for i in range(p_len+1)]
        if s_len == 0 and p_len == 0 or p == ".*":
            return True
        if p_len == 0 or p[0] == "*":
            return False
        j = 1
        result_matrix[0][0] = True
        for i in range(1, p_len+1):
            for j in range(s_len+1):
                if j > 0 :
                    if (p[i-1] == s[j-1] or p[i-1] == ".") and result_matrix[i-1][j-1] is True:
                        result_matrix[i][j] = True
                    elif p[i-1] == "*":
                        if result_matrix[i-2][j] is True or (p[i-2] == s[j-1] or p[i-2] == ".") and (result_matrix[i-1][j] is True or result_matrix[i][j-1] is True):
                            result_matrix[i][j] = True
            if p[i-1] == "*":
                result_matrix[i][0] = result_matrix[i-2][0]
        print result_matrix
        return result_matrix[i][j]

if __name__ == "__main__":
    s = Solution()
    print s.isMatch("aaaa", "aaaaa")


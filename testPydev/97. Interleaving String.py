class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        inter_matrix = [[False for i in range(len(s1) + 1)] for j in range(len(s2) + 1)]
        s3 = "0" + s3
        s1 = "0" + s1
        s2 = "0" + s2
        for i in range(len(inter_matrix)):
            for j in range(len(inter_matrix[0])):
                if i == 0 and j == 0:
                    inter_matrix[i][j] = True
                elif i == 0:
                    if s3[j] == s1[j]:
                        inter_matrix[i][j] = inter_matrix[i][j-1]
                elif j == 0:
                    if s3[i] == s2[i]:
                        inter_matrix[i][j] = inter_matrix[i-1][j]
                elif s3[i+j] == s1[j] and inter_matrix[i][j-1] or s3[i+j] == s2[i] and inter_matrix[i-1][j]:
                    print s3[i+j] + " : " + s1[j] + " : " + s2[i]
                    inter_matrix[i][j] = True
        print inter_matrix
        return inter_matrix[len(s2) - 1][len(s1) - 1]

if __name__ == "__main__":
    s = Solution()
    # print s.isInterleave("aabcc", "dbbca", "aadbbcbcac")
    # print s.isInterleave("aabcc", "dbbca", "aadbbbaccc")
    print s.isInterleave("db", "b", "cbb")
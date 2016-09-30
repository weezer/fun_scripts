class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) == 0:
            return 0
        if len(haystack) == 0 or len(needle) == 0:
            return -1
        p_needle = 0
        for i in range(len(haystack)):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1

if __name__ == "__main__":
    s = Solution()
    print s.strStr("mississippi", "issip")
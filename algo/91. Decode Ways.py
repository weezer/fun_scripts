class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_len = len(s)
        if s_len == 0 or s[0] == "0":
            return 0
        s_ways = [1 for i in range(s_len)]
        for i in range(1, s_len):
            if s[i-1:i+1] == "10" or s[i-1:i+1] == "20":
                s_ways[i] = s_ways[i-2]
            elif s[i] == "0":
                return 0
            elif s[i] != "0" and "26" >= s[i-1:i+1] > "10":
                s_ways[i] = s_ways[i-2] + s_ways[i-1]
            else:
                s_ways[i] = s_ways[i-1]
        return s_ways[i]


if __name__ == "__main__":
    s = Solution()
    print s.numDecodings("227")
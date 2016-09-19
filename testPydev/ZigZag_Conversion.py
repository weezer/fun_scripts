class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if len(s) <= 1 or numRows <= 1:
            return s
        rlst = []
        for i in range(numRows):
            pos = i
            gap1 = 2 * numRows - (i + 1) * 2
            gap2 = 2 * numRows - 2 - gap1
            gaps = [gap1, gap2]
            interval = 0
            while pos < len(s):
                if gaps[interval] != 0:
                    rlst.append(s[pos])
                    pos += gaps[interval]
                interval = (interval + 1) % 2
        return ''.join(rlst)


str1 = "PAYPALISHIRING"
str2 = "ABCD"
s = Solution()
print s.convert(str2, 3)

# PAHNAPLSIIGYIR

























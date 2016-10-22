class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        result = 0
        pos1 = 0
        for i in num1[::-1]:
            pos = 0
            for j in num2[::-1]:
                first = ord(i) - ord('0')
                second = ord(j) - ord('0')
                result += first * second * (10 ** pos) * (10 ** pos1)
                pos += 1
            pos1 += 1
        return str(result)

if __name__ == "__main__":
    s = Solution()
    print s.multiply("11", "12")
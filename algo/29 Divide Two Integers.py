class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        mul = 0
        INT_MAX = (1 << 31) - 1
        neg = False
        if dividend > 0 and divisor < 0 or dividend < 0 and divisor > 0:
            neg = True
        dividend = abs(dividend)
        divisor = abs(divisor)
        while dividend >= divisor:
            for i in range(50):
                if (divisor << i) > dividend:
                    print i
                    mul += 1 << i - 1
                    dividend -= divisor << i-1
                    break
        if neg:
            mul = -mul
        if mul > INT_MAX:
            mul = INT_MAX
        return mul
if __name__ == "__main__":
    s = Solution()
    print s.divide(-2147483648, -1)
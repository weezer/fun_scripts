class Solution(object):
    def binarySearchDivide(self, dividend, divisor):
        right_num = dividend
        left_num = 0
        while True:
            mid_num = (right_num + left_num) / 2
            if (mid_num + 1) * divisor > dividend > mid_num * divisor or mid_num * divisor == dividend:
                return mid_num
            else:
                if mid_num * divisor > dividend:
                    right_num = (right_num + left_num) / 2
                else:
                    left_num = (right_num + left_num) / 2


    def BinarySearchNoDivide(self, dividend, divisor):
        res = 0
        count = 1
        while dividend >= divisor:
            if divisor * (2 ** count) <= dividend < divisor * (2 ** (count + 1)):
                res += (2 ** count)
                dividend -= divisor * (2 ** count)
                count = 0
            else:
                count += 1
        return res


    def divide(self, dividend, divisor):
        if dividend == 0 or divisor == 0 or divisor > dividend > 0:
            return 0

        res = 0
        count = 0
        sign = (-1, 1)[0 > dividend]
        sign *= (-1, 1)[0 > divisor]
        abs_dividend = abs(dividend)
        abs_divisor = abs(divisor)
        while abs_dividend >= abs_divisor:
            if abs_divisor == abs_dividend:
                return (res + 1) * sign
            elif abs_divisor < abs_dividend < abs_divisor + abs_divisor:
                return (res + 1) * sign
            elif abs_divisor * (2 << count) <= abs_dividend < abs_divisor * (2 << (count + 1)):
                res += (2 << count)
                abs_dividend -= abs_divisor * (2 << count)
                count = 0
            else:
                count += 1
        return res

    def divide2(self, dividend, divisor):
        INT_MAX = (1 << 31) - 1
        if divisor == 0:
            return INT_MAX
        neg_sign = dividend > 0 and divisor < 0 or dividend < 0 and divisor > 0
        abs_dividend, abs_divisor = abs(dividend), abs(divisor)
        answer, shift = 0, 31
        while shift >= 0:
            if abs_dividend >= abs_divisor << shift:
                abs_dividend -= abs_divisor << shift
                answer += 1 << shift
            shift -= 1
        if neg_sign:
            answer = -answer
        if answer > INT_MAX:
            return INT_MAX
        return answer



if __name__ == "__main__":
    solu = Solution()
    # print solu.binarySearchDivide(-123, 3)
    # print solu.BinarySearchNoDivide(-123, 3)
    print solu.divide2(-2147483648, -1)

#2147483647
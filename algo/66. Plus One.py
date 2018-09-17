class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = 0
        mul = 10
        len_digits = len(digits)
        r_answer = []
        for i in range(len_digits):
            num += digits[len_digits - i - 1] * pow(mul, i)
        num += 1
        while num > 0:
            residue = num % 10
            num /= 10
            r_answer.append(residue)
        return r_answer[::-1]

if __name__ == "__main__":
    s = Solution()
    print s.plusOne([1,2,3])
class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        reverse_digits = digits[::-1]
        if reverse_digits[0] + 1 == 10:
            carry = 1
        else:
            carry = 0
        for pos, val in enumerate(reverse_digits):
            if val+carry == 10:
                carry = 1
                reverse_digits[pos] = 0
            else:
                carry = 0
                reverse_digits[pos] = val
        if carry == 1:
            reverse_digits.append(1)
        print reverse_digits[::-1]

if __name__ == "__main__":
    s = Solution()
    s.plusOne([9,9,9])
class Solution:
    # @param x, an integer
    # @return an integer
    def sqrt(self, x):
        left, right = 0, x
        while left <= right:
            mid = (left + right) // 2
            tmp = mid * mid
            if tmp == x:
                return mid
            if tmp > x:
                right = mid - 1
            if tmp < x:
                left = mid + 1
        return right

if __name__ == "__main__":
    s = Solution()
    print s.sqrt(5)
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        result_str = ""
        x = [str(i) for i in range(1, n+1)]
        while len(x) > 0:
            fac_result = self.factorial(n-1)
            for i in range(1, n+1):
                if i * fac_result >= k:
                    result_str += x.pop(i-1)
                    k -= (i-1) * fac_result
                    n -= 1
                    break

        print result_str

    def factorial(self, n):
        result = 1
        while n > 1:
            result *= n
            n -= 1
        return result

if __name__ == "__main__":
    s = Solution()
    s.getPermutation(3, 6)


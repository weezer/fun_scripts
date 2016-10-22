class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permuteUnique(self, num):
        self.result = []
        if num is None:
            return []
        if len(num) == 0:
            return [[]]
        self.permutation([], sorted(num))
        return self.result

    def permutation(self,  temp, num):
        if len(num) == 0:
            self.result.append(temp)
        else:
            for i in range(len(num)):
                if i > 0 and num[i] == num[i - 1]:
                    continue
                self.permutation( temp + [num[i]], num[:i] + num[i + 1:])

if __name__ == "__main__":
    s = Solution()
    print s.permuteUnique([3,3,0,3])
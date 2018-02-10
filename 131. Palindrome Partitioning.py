class Solution(object):
    def __init__(self):
        self.ans = []
        self.kv = {}

    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        self.helper(s, [])
        print self.ans

    def helper(self, s, result):
        len_s = len(s)
        if not s:
            self.ans.append(result)
            return
        for i in range(1, len_s+1):
            if self.kv.get(s[:i]) or self.isPalindrome(s[:i]):
                result2 = result[:]
                result2.append(s[:i])
                self.helper(s[i:], result2)

    def isPalindrome(self, s):
        if s == s[::-1]:
            self.kv[s] = 1
            return True
        else:
            return False

if __name__ == "__main__":
    s = Solution()
    s.partition("bbb")
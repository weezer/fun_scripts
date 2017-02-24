class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if s1 == s2:
            return True
        if len(s1) != len(s2):
            return False
        if sorted(s1) != sorted(s2):
            return False

        for i in range(1, len(s1)):
            s11 = s1[:i]
            s12 = s1[i:]
            s21 = s2[:i]
            s22 = s2[i:]
            if self.isScramble(s11, s21) and self.isScramble(s12, s22):
                return True
            s21 = s2[-i:]
            s22 = s2[:-i]
            if self.isScramble(s11, s21) and self.isScramble(s12, s22):
                return True
        return False

if __name__ == "__main__":
    s = Solution()
    print s.isScramble("acb", "bac")
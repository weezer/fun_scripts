import collections
class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        return self.rotate_word(s1, s2)

    def rotate_word(self, s1, s2):
        print s1, s2
        if s1 == s2:
            return True
        if collections.Counter(s1) == collections.Counter(s2):
            len_s1 = len(s1)
            for i in range(1, len_s1):
                if (self.rotate_word(s1[:i], s2[:i]) and self.rotate_word(s1[i:], s2[i:])) or (self.rotate_word(s1[:i], s2[-i:]) and self.rotate_word(s1[i:], s2[:-i])):
                    return True
        return False

if __name__ == "__main__":
    s = Solution()
    print s.isScramble("abb", "bab")
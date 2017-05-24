class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        _s = filter(lambda x: x.isalpha(), s)
        _s = _s.lower()
        start = 0
        end = len(_s) - 1
        print _s
        while start < end:
            if _s[start] != _s[end]:
                return False
            start += 1
            end -= 1
        return True

    def isPalindrome2(self, s):
        s = filter(lambda x : x.isalnum(), s)
        s = s.lower()
        if not s:
            return True
        min = 0
        max = len(s) - 1
        print s
        while min <= max:
            if s[min] != s[max]:
                return False
            min += 1
            max -= 1
        return True

if __name__ == "__main__":
    s = Solution()
    print s.isPalindrome2("A man, a plan, a canal: Panama")
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp_lst = [0] * len(s)
        lst = []
        max_num = 0
        for i in range(len(s)):
            if s[i] == "(":
                lst.append(i)
            elif s[i] == ")" and len(lst) > 0:
                pos = lst.pop()
                dp_lst[i] = 2 + dp_lst[pos-1] + dp_lst[i-1]
                max_num = max(dp_lst[i], max_num)
            elif s[i] == ")" and len(lst) == 0:
                continue
        return max_num


if __name__ == "__main__":
    s = Solution()
    s1 = "((())))((((())))"
    s2 = "()(())"
    print s.longestValidParentheses(s1)
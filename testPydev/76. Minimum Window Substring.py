class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        p_head, p_tail = 0, 0
        t_dict = dict.fromkeys(t, 0)
        flag_set = set(t)
        ans = ""
        while p_head < len(s):
            if s[p_head] in t:
                t_dict[s[p_head]] += 1
                if s[p_head] in flag_set:
                    flag_set.remove(s[p_head])
            if len(flag_set) == 0:
                while p_tail < p_head:
                    if s[p_tail] in t:
                        if t_dict[s[p_tail]] == 1:
                            break
                        t_dict[s[p_tail]] -= 1
                    p_tail += 1
                if len(ans) == 0 or p_head - p_tail < len(ans):
                    ans = s[p_tail: p_head+1]
                t_dict[s[p_tail]] -= 1
                flag_set.add(s[p_tail])
                p_tail += 1
            p_head += 1
        return ans


if __name__ == "__main__":
    S = "ADOBECODEBANC"
    T = "ABC"
    s = Solution()
    print s.minWindow(S, T)
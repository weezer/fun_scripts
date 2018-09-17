import Queue
import collections
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        len_s = len(s)
        source_list = [0] * 26
        target_list = [0] * 26
        target_count = {}
        for i in t:
            target_list[ord(i) - ord('a')] = 1
            target_count[i] = target_count.get(i, 0) + 1
        window_count = {}
        left, right = 0, 0
        result = []
        while True:
            if right >= len_s:
                break
            if source_list != target_list:
                if target_count.get(s[right]):
                    window_count[s[right]] = window_count.get(s[right], 0) + 1
                    if window_count[s[right]] >= target_count[s[right]]:
                        source_list[ord(s[right]) - ord('a')] = 1
                right += 1
            else:
                result.append(s[left:right])
                window_count[s[left]] -= 1
                if window_count[s[left]] >= target_count[s[left]]:
                    source_list[ord(s[left]) - ord('a')] = 1
                else:
                    source_list[ord(s[left]) - ord('a')] = 0
                left += 1
                while left < right and (target_count.get(s[left]) is None):
                    left += 1
            print left, right
        print source_list
        print target_list
        print window_count
        print target_count
        print left, right
        print result
        print s[right - 1]

    def minimum2(self, s, t):
        t_kv, t_len = collections.Counter(t), len(t)
        left, r_left, r_right = 0, 0, 0
        for right, letter in enumerate(s, 1):
            if t_kv[letter] > 0:
                t_len -= 1
            t_kv[letter] -= 1
            if t_len == 0:
                while t_kv[s[left]] < 0:
                    t_kv[s[left]] += 1
                    left += 1
                if not r_right or (right - left) < (r_right - r_left):
                    r_left, r_right = left, right
        print r_left, r_right
        print t_kv
        return s[r_left: r_right]


if __name__ == "__main__":
    s = Solution()
    # s.minWindow("adobecodebanc","abc")
    print s.minimum2("adobecodebanc","abc")

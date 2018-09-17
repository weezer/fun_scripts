import collections
import Queue
class longestDoubleLetter(object):
    def __init__(self):
        pass

    def solution1(self, string):
        q = Queue.deque()
        max_len = 0
        for i in string:
            q.append(i)
            q_c = collections.Counter(q)
            while q_c > 2:
                q.popleft()
                q_c = collections.Counter(q)
            max_len = len(q)
        return max_len

    class Solution(object):
        def characterReplacement(self, s, k):
            """
            :type s: str
            :type k: int
            :rtype: int
            """
            s_kv = collections.defaultdict(list)
            len_s = len(s)
            max_len = 0
            for i in range(len_s):
                s_kv[s[i]].append(i)
                for k, v in s_kv:
                    len_v = len(v)
                for i in range(len_v):
                    l = v[i]
                r = i + k
                next_pos = i
                while v[next_pos] < r:
                    r += 1
                    next_pos += 1
                max_len = max(max_len, r - l)
            print max_len
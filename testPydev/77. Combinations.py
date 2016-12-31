class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        num_list = [i for i in range(1, n+1)]
        ans = [[]]
        for i in num_list:
            for j in range(len(ans)):
                tmp = ans[j][:]
                tmp.append(i)
                ans.append(tmp)
        return [x for x in ans if len(x) == 2]

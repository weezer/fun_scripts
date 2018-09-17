class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1_lst = version1.split(".")
        v2_lst = version2.split(".")
        len_v1 = len(v1_lst)
        len_v2 = len(v2_lst)
        cmp_len = min(len_v1, len_v2)
        for pos in range(cmp_len):
            if v1_lst[pos] > v2_lst[pos]:
                return 1
            elif v1_lst[pos] < v2_lst[pos]:
                return -1
        if len_v1 > len_v2:
            return 1
        elif len_v2 > len_v1:
            return -1
        else:
            return 0

if __name__ == "__main__":
    s = Solution()
    s.compareVersion()
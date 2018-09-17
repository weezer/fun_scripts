class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        kv = {}
        len_s = len(s)
        ans_lst = []
        for i in range(len_s - 9):
            kv[s[i: i+10]] = kv.get(s[i: i+10], 0) + 1
        for k, v in kv.items():
            if v > 1:
                ans_lst.append(k)
        return ans_lst

if __name__ == "__main__":
    s = Solution()
    s.finRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")
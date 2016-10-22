class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d= {}
        for i in strs:
            str_key = ''.join(sorted(list(i)))
            if d.has_key(str_key):
                d[str_key].append(i)
            else:
                d[str_key] = [i]
        return d.values()

if __name__ == "__main__":
    s = Solution()
    print s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])

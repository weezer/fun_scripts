class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        lst = input.split("\n")
        kv = {}
        max_length = 0
        print lst
        for i in lst:
            t_count = i.count("\t")
            kv[t_count] = i
            current_length = 0
            for j in range(t_count + 1):
                current_length += len(kv[j]) - j
            max_length = max(max_length, current_length + j)
        return max_length

if __name__ == "__main__":
    s = Solution()
    print s.lengthLongestPath("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext")
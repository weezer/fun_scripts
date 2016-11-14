class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        pathlst = path.split("/")
        remain_lst = []
        for i in pathlst:
            if i == '' or i == '.' or i == '..' and len(remain_lst) == 0:
                continue
            elif i == "..":
                remain_lst.pop()
            else:
                remain_lst.append(i)
        return "/" + "/".join(remain_lst)


if __name__ == "__main__":
    s = Solution()
    print s.simplifyPath("/a/./b/../../c/")
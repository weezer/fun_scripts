class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        lst = preorder.split(",")

        len_lst = len(lst)

        sharp_count = 0
        print len_lst
        print lst
        for i in range(len_lst-1, -1, -1):
            if lst[i] == "#":
                sharp_count += 1
            else:
                sharp_count -= 1
            print sharp_count

        if sharp_count == 1:
            return True
        return False

if __name__ == "__main__":
    s = Solution()
    s.isValidSerialization("9,#,92,#,#")
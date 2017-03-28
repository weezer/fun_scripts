class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self.result = []
        self.build_ip_stack(0, [s])
        return_result = []
        for i in self.result:
            flag = True
            for j in i:
                if int(j) > 255 or len(j) > 1 and j[0] == "0":
                    flag = False
            if flag:
                return_result.append(".".join(i))
        return return_result

    def build_ip_stack(self, step, lst):
        if step == 3:
            if len(lst[3]) > 3 or len(lst[3]) == 0:
                return
            else:
                self.result.append(lst)
                return
        for i in range(1,4):
            copy_lst = lst[:]
            replace_lst = [''.join(copy_lst[step][:i]), copy_lst[step][i:]]
            copy_lst[step:step+1] = replace_lst
            # print copy_lst
            self.build_ip_stack(step + 1, copy_lst)


if __name__ == "__main__":
    s = Solution()
    print s.restoreIpAddresses("010010")
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 0:
            return 'None'
        theNum = 1
        for i in range(n):
            theNum = self.str_generator(int(theNum))
        return theNum

    def str_generator(self, n):
        str_n = str(n)
        flag = str_n[0]
        count = 0
        answer = []
        for i in str_n:
            if i != flag:
                answer.append(count)
                answer.append(flag)
                flag = i
                count = 1
            else:
                count += 1
        answer.append(count)
        answer.append(flag)

        return ''.join(map(str, answer))


if __name__ == "__main__":
    s = Solution()
    print s.countAndSay(2)

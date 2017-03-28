class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0 or s[0] == '0':
            return 0
        dp = [1, 1]
        s_len = len(s)
        for i in range(2, s_len + 1):
            if 10 < int(s[i - 2:i]) <= 26 and s[i - 1] != '0':
                dp.append(dp[i - 2] + dp[i - 1])
            elif s[i - 2:i] == '10' or s[i - 2:i] == '20':
                dp.append(dp[i - 2])
            elif s[i - 1] != '0':
                dp.append(dp[i - 1])
            else:
                return 0
        print dp
        return dp[s_len]

    def wrong_numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        import collections
        num_chr = {str(i): ord('a') + i - 1 for i in range(1, 27)}
        s_lst = list(s)
        result = collections.deque()
        result.append(s_lst)
        result_set = set()
        while result:
            current = result.popleft()
            result_set.add(tuple(current))
            current_len = len(current)
            pos = 0
            while pos < current_len-1:
                part0 = current[:pos]
                part1 = ''.join(current[pos:pos+2])
                part2 = current[pos+2:]
                pos += 1
                if len(part1) > 2:
                    continue
                sum_up = part0 + [part1] + part2
                result.append(sum_up)
        count = 0
        for i in result_set:
            flag = True
            for j in i:
                if num_chr.get(j) is None:
                    flag = False
                    break
            if flag:
                count += 1

        print str(len(result_set)) + " : " + str(count)


if __name__ == "__main__":
    s = Solution()
    print s.numDecodings("12120")





class Solution(object):
    def makesquare(self, lst):
        lst = sorted(lst, reverse=True)

        edge_length = sum(lst) // 4
        if len(lst) < 4 or edge_length * 4 != sum(lst) or max(lst) > edge_length:
            return False
        for _ in range(3):
            return_lst = self.canmakenumber(lst, edge_length)
            if return_lst is False:
                return False
            for i in return_lst:
                lst.remove(i)
        return True

    def canmakenumber(self, lst, num):
        b = [0] * num
        b2 = [0] * num
        can_make = False
        for pos, i in enumerate(lst):
            for j in b:
                if j != 0 and j-1+i < num:
                    b2[j-1+i] = b[j-1] + i
                if b2[num-1] != 0:
                    can_make = True
                    break
            b2[i - 1] = i
            b = b2[:]
            if can_make:
                return_lst = self.findthesticks(b, lst[:pos+1])
                break
        if can_make:
            return return_lst
        return False

    def findthesticks(self, lst, input_stick):
        return_lst = []
        pos = len(lst) -1
        for i in input_stick[::-1]:
            if lst[pos] in input_stick:
                return_lst.append(lst[pos])
                break
            elif lst[pos - i] != 0:
                return_lst.append(i)
                pos -= i
        return return_lst


if __name__ == "__main__":
    L1 = [10, 6, 5, 5, 5, 3, 3, 3, 2, 2, 2, 2]
    L2 = [2,2,2,3,4,4,4,5,6]
    L3 = [2,2,2,2,2,6]
    L4 = [1, 1, 1, 1]
    L5 = []
    L6 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 5, 32, 4, 32, 2, 34, 4, 3, 43, 43, 2, 2, 34, 43, 2, 34, 43, 2, 34, 43, 24, 3, 24,
           32, 3, 21, 64, 6, 5, 5, 3]
    L7 = [2,2,2,2,2,2]
    L8 = [6,6,6,6,6,6]

    s = Solution()
    print s.makesquare(L8)



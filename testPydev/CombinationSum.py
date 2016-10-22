class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.result = []
        for i in range(len(candidates)):
            self.recursivesum([candidates[i]], candidates[i:], target)

        return self.result

    def recursivesum(self, temp_list, comblist, target):
        if sum(temp_list) == target:
            self.result.append(temp_list)
            return
        for i in range(len(comblist)):
            if sum(temp_list) + comblist[i] == target:
                result_list = temp_list[:]
                result_list.append(comblist[i])
                self.result.append(result_list)
            if sum(temp_list) + comblist[i] < target:
                test_list = temp_list[:]
                test_list.append(comblist[i])
                self.recursivesum(test_list[:], comblist[i:], target)


if __name__ == "__main__":
    s = Solution()
    bb = s.combinationSum([2,3,6,7], 7)
    for i in bb:
        print i
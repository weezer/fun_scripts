class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        matrix = [1] + [0] * target
        for i in range(1, target + 1):
            for j in nums:
                if j > i:
                    break
                if j == i:
                    matrix[i] += 1
                if j < i:
                    matrix[i] += matrix[i-j]
        return matrix[target]

    def generate_path(self, nums, target):
        global result
        result = []

        def dfs(nums, target, res):
            global result
            if sum(res) >= target:
                if sum(res) == target:
                    result.append(res)
                return
            for i in nums:
                copy_res = res[:]
                copy_res.append(i)
                dfs(nums, target, copy_res)
        dfs(nums, target, [])
        return result


if __name__ == "__main__":
    s = Solution()
    print s.combinationSum4([1,2,3], 7)
    print len(s.generate_path([1,2,3], 7))
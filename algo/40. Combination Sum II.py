class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.result = []
        self.helper(sorted(candidates), target, 0, [])
        return self.result

    def helper(self, candidates, target, start, stack):
        for i in range(len(candidates[start:])):
            if i!= 0 and candidates[start:][i] == candidates[start:][i-1]:
                continue
            if sum(stack) + candidates[start:][i] == target:
                self.result.append(stack + [candidates[start:][i]])
            elif sum(stack) + candidates[start:][i] < target:
                self.helper(candidates, target, start + 1 + i, stack + [candidates[start:][i]])

    def combinationSum3(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        return self.dfs(candidates,0,[],[],target)
    def dfs(self, candidates,start,res,ans,target):
        if target<0:
            return
        if target==0:
            res.append(ans)
            return
        for i in xrange(start,len(candidates)):
            if i!=start and candidates[i]==candidates[i-1]:
                continue
            self.dfs(candidates,i+1,res,ans+[candidates[i]],target-candidates[i])
        return res

if __name__ == "__main__":
    s = Solution()
    print s.combinationSum2([10,1,2,7,6,1,5], 8)
    print s.combinationSum2([1,1,1,2,3], 3)
    print s.combinationSum3([10,1,2,7,6,1,5], 8)
    print s.combinationSum3([1,1,1,2,3], 3)
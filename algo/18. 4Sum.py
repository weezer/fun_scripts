class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        r_ans = []
        def findKSum(arr, k, target, ans):
            len_arr = len(arr)
            if len_arr < k or k < 2:
                return
            if k == 2:
                left, right = 0, len_arr - 1
                while left < right:
                    if arr[left] + arr[right] == target:
                        tmp = ans[:]
                        tmp.append(arr[left])
                        tmp.append(arr[right])
                        r_ans.append(tmp)
                        left += 1
                        right -= 1
                        while left < right and arr[left - 1] == arr[left]:
                            left += 1
                        while left < right and arr[right + 1] == arr[right]:
                            right -= 1
                    elif arr[left] + arr[right] > target:
                        right -= 1
                        while left < right and arr[right + 1] == arr[right]:
                            right -= 1
                    else:
                        left += 1
                        while left < right and arr[left - 1] == arr[left]:
                            left += 1
            else:
                for i in range(len_arr - k + 1):
                    if target < arr[i] * k or target > arr[-1] * k:
                        break
                    if i == 0 or i > 0 and arr[i - 1] != arr[i]:
                        tmp = ans[:]
                        tmp.append(arr[i])
                        findKSum(arr[i + 1:], k - 1, target - arr[i], tmp)

        findKSum(nums, 4, target, [])
        return r_ans


if __name__ == "__main__":
    s = Solution()
    print s.fourSum([-3,-2,-1,0,0,1,2,3], 0)

class BinaryRange(object):
    def findRange(self, nums, target):
        left = self.findtheleft(nums, target)
        right = self.findtheright(nums, target)
        return [left, right]

    def findtheleft(self, nums, target):
        left = 0
        right = len(nums) - 1
        if nums[left] == target:
            return left
        if nums[left] > target:
            return -1
        while left <= right:
            mid = (left + right) / 2
            if mid > 0:
                if nums[mid - 1] < target and nums[mid] == target:
                    return mid

            if target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    def findtheright(self, nums, target):
        left = 0
        right = len(nums) - 1
        if nums[right] == target:
            return right
        if nums[right] < target:
            return -1
        while left <= right:
            mid = (left + right) / 2
            if mid < len(nums) - 1:
                if nums[mid + 1] > target and nums[mid] == target:
                    return mid
            if target < nums[mid]:
                right = mid - 1
            else:
                left = mid
        return -1

if __name__ == "__main__":
    s = BinaryRange()
    print s.findRange([0,1,2,3,4,5,6,7,8,8,9], 8)
    print s.findRange([0,0], 1)
    print s.findRange([1,3,4], 1)
    print s.findRange([1,1,1,1,1,1,1], 1)
    print s.findRange([1], 0)
    print s.findRange([0,1,1,3,3,3], 3)
    print s.findRange([5,7,7,8,8,10], 8)

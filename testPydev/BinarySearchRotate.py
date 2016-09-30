class BinarySearchRotate(object):
    def binarySearchRotate(self, nums, target):
        left = 0
        right = len(nums) - 1
        mid = (left + right) / 2
        while left <= right:
            if nums[mid] == target:
                return mid
            if nums[mid] > nums[left] and nums[mid] > nums[right]:
                if nums[left] <= target < nums[mid]:
                    right = mid
                else:
                    left = mid + 1
            else:
                if target < nums[mid]:
                    right = mid
                else:
                    left = mid + 1
            mid = (left + right) / 2
            print left, right
        return -1

def rotate(l, n):
    return l[-n:] + l[:-n]

if __name__ == "__main__":
    s = BinarySearchRotate()
    lst = rotate([0,1,2,3,4,5,6,7], 5)
    print lst
    print s.binarySearchRotate(lst, 0)


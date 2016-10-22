# Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.

class Solution(object):
    def trappingwater(self, height):
        size = 0
        for i in range(1, len(height)):
            left = max(height[:i])
            right = max(height[i:])
            if height[i] < min(left, right):
                size += min(left, right) - height[i]
        return size


if __name__ == "__main__":
    s = Solution()
    print s.trappingwater([0,1,0,2,1,0,1,3,2,1,2,1])
    print s.trappingwater([2, 0, 2])
    print s.trappingwater([5,4,1,2])
    print s.trappingwater([5,2,1,2,1,5])
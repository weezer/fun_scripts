class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        lv = height[left]
        rv = height[right]
        total = lv + rv
        floor_toal = total
        while left < right:
            if lv > rv:
                right -= 1
                total += height[right]
                rv = max(rv, height[right])
                floor_toal += rv
            else:
                left += 1
                total += height[left]
                lv = max(lv, height[left])
                floor_toal += lv
        return floor_toal - total

if __name__ == "__main__":
    s = Solution()
    print s.trap([5,2,1,2,1,5])
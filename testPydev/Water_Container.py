class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        end = len(height) - 1
        start = 0
        max_volume = 0
        while end > start:
            print end
            if height[end] >= height[start]:
                v_height = height[start]
                start += 1
            else:
                v_height = height[end]
                end -= 1
            if max_volume < (end - start + 1) * v_height:
                max_volume = (end - start + 1) * v_height
        return max_volume


if __name__ == "__main__":
    s = Solution()
    s.maxArea([1,1])
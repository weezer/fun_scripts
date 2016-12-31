class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        go_up = False
        go_down = False
        if len(heights) > 1:
            prev = heights[0]
            max_size = heights[0]
            zero_pos= 0
        for pos in range(1, len(heights)):
            if heights[pos] == 0 and prev > heights[pos]:
                max_size = max(pos - zero_pos * min(heights[zero_pos:pos]), max_size)
                prev = 0
                continue

            if prev > heights[pos]:
                go_down = True
                if go_up is True:
                    for i in range(pos-1, start-1, -1):
                        max_size = max(min(heights[i:pos]) * (pos - i), max_size)
                max_size = max

            if prev < heights[pos]:
                if prev == 0:
                    zero_pos = pos
                if go_up is True:
                    prev = heights[pos]
                    continue
                else:
                    start = pos - 1
                    go_up = True

            if prev == heights[pos]:
                continue

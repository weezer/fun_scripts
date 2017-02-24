class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        dummy_stack = heights[:] + [0]
        stack = []
        largest = 0
        pos = 0
        while pos < len(dummy_stack):
            if not stack or dummy_stack[pos] > dummy_stack[stack[-1]]:
                stack.append(pos)
                pos += 1
            else:
                cur_pos = stack.pop()
                largest = max(largest, dummy_stack[cur_pos] * (not stack and pos or pos - stack[-1] - 1))
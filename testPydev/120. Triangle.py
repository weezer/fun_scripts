class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if len(triangle) == 0 or len(triangle[0]) == 0:
            return None
        len_triangle = len(triangle)
        stack = [0] * len_triangle
        for i in range(len(triangle)):
            if i == 0 :
                stack[0] = triangle[0][0]
                continue
            for j in range(i, -1, -1):
                if j == 0:
                    stack[j] += triangle[i][j]
                elif j == i:
                    stack[j] = stack[j-1] + triangle[i][j]
                else:
                    stack[j] = min(stack[j-1], stack[j]) + triangle[i][j]
        return min(stack)

if __name__ == "__main__":
    s = Solution()
    a =[
]
    print s.minimumTotal(a)
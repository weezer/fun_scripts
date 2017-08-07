class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        visited = [0 for i in range(numCourses)]
        pair_map = {i:[] for i in range(numCourses)}
        import Queue
        q_course = Queue.deque()
        for i in prerequisites:
            pair_map[i[1]].append(i[0])
            visited[i[0]] = visited[i[0]] + 1
        for i in range(numCourses):
            if visited[i] == 0:
                q_course.append(i)
        zero_list = len(q_course)
        while len(q_course) > 0:
            current = q_course.popleft()
            link = pair_map[current]
            for i in link:
                visited[i] -= 1
                if visited[i] == 0:
                    zero_list += 1
                    q_course.append(i)
        if zero_list != numCourses:
            return False
        return True

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course = defaultdict(list)
        indegree = [0]*numCourses
        for c, pre in prerequisites:
            course[pre].append(c)
            indegree[c]+=1

        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        cnt = 0
        while queue:
            curr = queue.popleft()
            cnt+=1

            for next_course in course[curr]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    queue.append(next_course)
        
        return cnt == numCourses
            
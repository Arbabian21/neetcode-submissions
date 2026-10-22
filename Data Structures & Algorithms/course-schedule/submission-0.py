class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseMap = {i:[] for i in range(numCourses)}
        for course, preReq in prerequisites:
            courseMap[course].append(preReq)

        visited = set()

        def dfs(course):
            if course in visited: return False
            if courseMap[course] == []: return True

            visited.add(course)
            for preReq in courseMap[course]:
                if not dfs(preReq): return False
            courseMap[course] = []
            visited.remove(course)
            return True
            
        for course in range(numCourses):
            if not dfs(course): return False
        return True
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # dfs
            adjacencyMap = {i:[] for i in range(n)}
            visited = set()
            for node1,node2 in edges:
                adjacencyMap[node1].append(node2)
                adjacencyMap[node2].append(node1)


            def dfs(node):
                visited.add(node)
                for adjacentNode in adjacencyMap[node]:
                    if  not adjacentNode in visited:
                        dfs(adjacentNode)
            
            res = 0

            for node in range(n):
                if not node in visited:
                    dfs(node)
                    res += 1
            return res
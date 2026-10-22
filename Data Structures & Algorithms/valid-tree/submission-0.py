class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n: return True

        TreeMap = {i:[] for i in range(n)}
        for node1, node2 in edges:
            TreeMap[node1].append(node2)
            TreeMap[node2].append(node1)

        visited = set()
        def dfs(currNode, prevNode):
            if currNode in visited: return False

            visited.add(currNode)
            for adjacentNode in TreeMap[currNode]:
                if adjacentNode == prevNode: continue
                if not dfs(adjacentNode, currNode): return False
            return True

        return dfs(0,-1) and len(visited) == n

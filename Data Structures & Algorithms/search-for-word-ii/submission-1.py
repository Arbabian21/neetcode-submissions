class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

    def addWord(self,word):
        curr = self

        for letter in word:
            node = curr.children.get(letter)
            if not node:
                node = TrieNode()
                curr.children.update({letter: node})
            curr = node
        curr.endOfWord = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            root.addWord(word)

        ROWS = len(board)
        COLS = len(board[0])

        results = set()
        path = set()

        def dfs(r, c, currNode, word):
            if (r < 0 or c < 0 or
               r == ROWS or c == COLS or 
               (r,c) in path or board[r][c] not in currNode.children):
               return
            
            path.add((r,c))
            node = currNode.children.get(board[r][c])
            word += board[r][c]
            if node.endOfWord: results.add(word)

            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)

            path.remove((r,c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")

        return list(results)






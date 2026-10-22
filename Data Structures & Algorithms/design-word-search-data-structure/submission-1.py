class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfString = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for letter in word:
            node = curr.children.get(letter)
            if not node:
                node = TrieNode()
                curr.children.update({letter : node})
            curr = node
        curr.endOfString = True

    def search(self, word: str) -> bool:

        def dfs(index, root):
            curr = root
            for i in range(index, len(word)):

                if word[i] == ".":
                    for value in curr.children.values():
                        if dfs(i + 1, value): return True
                    return False
                else: 
                    node = curr.children.get(word[i])
                    if not node: return False
                    curr = node
            return curr.endOfString
        return dfs(0, self.root)

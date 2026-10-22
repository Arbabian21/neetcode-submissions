class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfString = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for letter in word:
            node = curr.children.get(letter)
            if node == None:
                node = TrieNode()
                curr.children.update({letter: node})
            curr = node
        curr.endOfString = True

    def search(self, word: str) -> bool:
        curr = self.root
        for letter in word:
            node = curr.children.get(letter)
            if node == None: return False
            curr = node
        return curr.endOfString

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for letter in prefix:
            node = curr.children.get(letter)
            if node == None: return False
            curr = node
        return True
        
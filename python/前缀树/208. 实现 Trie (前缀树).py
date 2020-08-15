class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for i in word:
            if i not in node:
                node[i] = {}
            node = node[i]
        node["-"] = True


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for i in word:
            if i not in node:
                return False
            node = node[i]
        return "-" in node


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for i in prefix:
            if i not in node:
                return False
            node = node[i]
        return True

trie = Trie()
trie.insert("apple")
trie.search("apple")
trie.search("app")
trie.startsWith("app")
trie.insert("app")
trie.search("app")

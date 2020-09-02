import collections
from typing import List
class Solution:
    def longestWord(self, words: List[str]) -> str:
        res=''
        trie=Trie()
        for word in words:
            trie.insert(word)
        for word in words:
            if trie.search(word):
                if len(word) > len(res):
                    res=word
                elif len(word)==len(res) and word < res:
                    res=word
        return res

class TrieNode:
    def __init__(self):
        self.end=False
        self.children=collections.defaultdict(TrieNode)

class Trie:
    def __init__(self):
        self.root=TrieNode()

    def insert(self, word: str) -> None:
        node=self.root
        for s in word:
            node=node.children[s]
        node.end=True

    def search(self, word: str) -> bool:
        node=self.root
        for s in word:
            node=node.children.get(s)
            if node is None or not node.end:
                return False
        return True

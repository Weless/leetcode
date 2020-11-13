from typing import List
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if len(wordList) < 2 or endWord not in wordList: return 0
        from collections import deque,defaultdict
        d = defaultdict(list)
        tmp = [beginWord] + wordList if beginWord not in wordList else wordList
        i = 0
        s = set()
        while i < len(tmp):
            cur = tmp[i]
            s.add(cur)
            for word in tmp[:i]+tmp[i+1:]:
                if self.isSimilar(cur,word) and word not in s:
                    d[cur].append(word)
            i+=1
        q = deque()
        q.appendleft(beginWord)
        level = 1
        while q:
            for _ in range(len(q)):
                word = q.pop()
                if word == endWord:
                    return level
                for item in d[word]:
                    q.appendleft(item)
            level += 1
        return 0

    # 找到和当前单词只差一个字母的单词
    def isSimilar(self,word1,word2):
        i = 0
        ok = 0
        while i<len(word1):
            if word1[i] != word2[i]:
                ok+=1
            if ok == 2:
                return False
            i+=1
        return True

s = Solution()
beginWord = "hot"
endWord = "dog"
wordList = ["hot","dog","dot"]
print(s.ladderLength(beginWord,endWord,wordList))
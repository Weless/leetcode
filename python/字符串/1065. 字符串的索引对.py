from typing import List
class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        ans = []
        for word in words:
            i = 0
            while i< len(text):
                j = i+len(word)
                if j<=len(text):
                    tmp = text[i:j]
                    if tmp == word:
                        ans.append([i,j-1])
                i+=1
        ans.sort(key=lambda x:(x[0],x[1]))
        return ans

# 字典树
class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        Trie = lambda: collections.defaultdict(Trie)
        trie = Trie()  # 初始化嵌套字典结构
        for word in words:
            functools.reduce(dict.__getitem__, word, trie)['*'] = word

        ans = []
        for i, c in enumerate(text):
            cur = trie  # 初始化搜索位置
            idx = i
            while c in cur:
                cur = cur[c]  # 向下搜索
                if '*' in cur:  # 找到符合题意的索引对
                    ans.append([i, idx])
                # 更新到下一个字母
                idx += 1
                if idx == len(text): break  # text的边界
                c = text[idx]

        return ans

s = Solution()
text = "ababa"
words = ["aba","ab"]
print(s.indexPairs(text,words))
            

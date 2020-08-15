class UnionFind:
    def __init__(self,N):
        self.num = N       # 记录连通分量数
        self.id = [0] * N  # 分组
        self.sz = [0] * N  # 记录树的大小
        for i in range(N):
            self.id[i] = i
            self.sz[i] = 1
    def count(self):
        return self.num
    def connected(self,p,q):
        return self.find(p) == self.find(q)
    def find(self,p):
        while p != self.id[p]:
            p = self.id[p]
        return p
    def union(self,p,q):
        i = self.find(p)
        j = self.find(q)
        # 如果两个组号相等，直接返回
        if i == j: return
        # 将小树作为大树的子树
        if (self.sz[i] < self.sz[j]):
            self.id[i] = j
            self.sz[j] += self.sz[i]
        else:
            self.id[j] = i
            self.sz[i] += self.sz[j]
        self.num -= 1

if __name__ == '__main__':
    uf = UnionFind(8)
    uf.union(2,3)
    uf.union(1,0)
    uf.union(0,4)
    uf.union(5,7)
    print(uf.count())
class UnionFind:
    def __init__(self,N):
        self.num = N       # 记录连通分量数
        self.id = [0] * N  # 分组
        for i in range(N):
            self.id[i] = i
    def count(self):
        return self.num
    def connected(self,p,q):
        return self.find(p) == self.find(q)
    def find(self,p):
        while p != self.id[p]:
            p = self.id[p]
        return p
    def union(self,p,q):
        pRoot = self.find(p)
        qRoot = self.find(q)
        # 如果两个组号相等，直接返回
        if pRoot == qRoot: return
        self.id[pRoot] = self.id[qRoot]
        self.num -= 1

if __name__ == '__main__':
    uf = UnionFind(8)
    uf.union(2,3)
    uf.union(1,0)
    uf.union(0,4)
    uf.union(5,7)
    print(uf.count())
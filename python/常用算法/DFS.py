def dfs(adj, start):
    visited = set()
    stack = [[start, 0]]
    while stack:
        (v, next_child_idx) = stack[-1]
        if (v not in adj) or (next_child_idx >= len(adj[v])):
            stack.pop()
            continue
        next_child = adj[v][next_child_idx]
        stack[-1][1] += 1
        if next_child in visited:
            continue
        print(next_child)
        visited.add(next_child)
        stack.append([next_child, 0])

#
# graph = {1: [4, 2], 2: [3, 4], 3: [4], 4: [5]}
# dfs(graph, 1)


# 递归版深度优先

def rec_dfs(G,s,S=None):
    if S is None:S = set()
    S.add(s)
    for u in G[s]:
        if u in S:continue
        rec_dfs(G,u,S)


# 迭代版深度优先
def iter_dfs(G,s):
    S,Q=set(),[]
    Q.append(s)
    while Q:
        u = Q.pop()
        if u in S:continue
        S.add(u)
        Q.extend(G[u])
        yield u

if __name__ == "__main__":
    a, b, c, d, e, f, g, h, i = range(9)
    G = [{b, c, d, e, f},  # a
         {c, e},           # b
         {d},              # c
         {e},              # d
         {f},              # e
         {c, g, h},        # f
         {f, h},           # g
         {f, g}            # h
         ]
    print(list(iter_dfs(G,a)))       # [0, 5, 7, 6, 2, 3, 4, 1]
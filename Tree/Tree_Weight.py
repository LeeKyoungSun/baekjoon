#1289번 트리의 가중치
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def dfs(u):
    global ans
    visited[u] = True
    p = []
    for i in range(len(edges[u])):
        v = edges[u][i]
        c = costs[u][i]
        if visited[v]:
            continue

        dfs(v)
        dp[u] += (dp[v] * c) % MOD
        dp[u] %= MOD

        p.append((dp[v] * c) % MOD)
    ans += dp[u]
    ans %= MOD

    sum_v = 0
    for v in p:
        sum_v += ((dp[u] - v + MOD) % MOD * v) % MOD
        sum_v %= MOD

    sum_v *= 500000004
    sum_v %= MOD

    ans += sum_v
    ans %= MOD

    dp[u] += 1
    dp[u] %= MOD


MOD = 1000000007
N = int(input())
ans = 0
visited = {i: False for i in range(1, N + 1)}
dp = [0 for _ in range(N + 1)]
edges = {i: [] for i in range(1, N + 1)}
costs = {i: [] for i in range(1, N + 1)}
for _ in range(N - 1):
    a, b, c = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)
    costs[a].append(c)
    costs[b].append(c)

dfs(1)
print(ans)
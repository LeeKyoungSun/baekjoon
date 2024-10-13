#1693 트리 색칠하기
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def solution():
    n = int(input())

    # 노드 100,000개는 log_2(100,000) = 16.xxx
    # 16개 색깔로 색칠 가능하다.
    # dp[i][color] : i번째 노드를 color로 색칠했을 때 최소값
    dp = [[0] * 16 for i in range(n)]

    # 방문 여부를 체크해준다.
    visit = [False for i in range(n)]

    # 인접 리스트로 트리의 간선을 기록해준다.
    tree = [[] for i in range(n)]
    for i in range(n - 1):
        a, b = map(int, input().split())
        tree[a - 1].append(b - 1)
        tree[b - 1].append(a - 1)

    # 트리를 순회해준다.
    def dfs(here):
        visit[here] = True

        for there in tree[here]:  # here와 인접한 노드를 대상으로
            if not visit[there]:  # 방문하지 않았다면
                dfs(there)  # dfs를 실행 시켜준다.

                # 최소값을 찾아준다.
                for pre_color in range(16):
                    m_num = 100000000
                    for color in range(16):
                        if pre_color != color:  # 이전에 칠한 색깔과 현재 칠한 색깔이 다르고
                            if m_num > dp[there][color]:  # 최소값이라면 최소값을 업데이트
                                m_num = dp[there][color]
                    dp[here][pre_color] += m_num  # 최솟값을 더해준다.

        # 마지막에 업데이트 해야한다.
        for color in range(16):
            dp[here][color] += color + 1
        return

    dfs(0)
    return min(dp[0])


print(solution())
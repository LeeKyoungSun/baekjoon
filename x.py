# flake8 코드 스타일이 적용되어 있습니다.
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

# 바퀴를 배열 형태로 선언
wheel = ['?'] * N
index = 0
check = True

# 상덕이가 적어놓은 종이에 해당하는 행운위 바퀴가 없는 경우
# 우리는 바퀴의 역방향으로 값을 채워 넣음을 잊지말기!
for k in range(K):
    cnt, alpha = input().split()
    index = (index + int(cnt)) % N
    # 1. 같은 수가 2번이상 들어갈 때
    if wheel[index] == '?':
        wheel[index] = alpha
    elif wheel[index] == alpha:
        continue
    else:
        check = False
        break

# 2. 바퀴를 2번 돌렸을 때 이미 숫자가 있는 칸에 새로운 숫자가 들어갈 때
for n in range(N - 1):
    if wheel[n] == '?':
        continue
    for j in range(n + 1, N):
        if wheel[n] == wheel[j]:
            check = False
            break

if not check:
    print('!')
else:
    for i in range(N):
        print(wheel[index], end='')
        index -= 1
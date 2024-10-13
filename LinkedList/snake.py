from collections import deque

n = int(input())
k = int(input())

graph = [[0] * n for _ in range(n)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for i in range(k):
    a, b = map(int, input().split())
    graph[a - 1][b - 1] = 2

l = int(input())
dirDict = dict()
queue = deque()
queue.append((0, 0))

for i in range(l):
    x, c = input().split()
    dirDict[int(x)] = c

x, y = 0, 0
graph[x][y] = 1
cnt = 0
direction = 0

def turn(alpha):
    global direction
    if alpha == 'L':
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4


while True:
    cnt += 1
    x += dx[direction]
    y += dy[direction]

    if x < 0 or x >= n or y < 0 or y >= n:
        break

    if graph[x][y] == 2:
        graph[x][y] = 1
        queue.append((x, y))
        if cnt in dirDict:
            turn(dirDict[cnt])

    elif graph[x][y] == 0:
        graph[x][y] = 1
        queue.append((x, y))
        tx, ty = queue.popleft()
        graph[tx][ty] = 0
        if cnt in dirDict:
            turn(dirDict[cnt])

    else:
        break

print(cnt)

n= int(input()) #보드 크기 입력받기
board = [([0] * n) for _ in range(n)] #보드 생성
apple = []
k = int(input())
for _ in range(k);
    input_row, input_col = map(int, input().split()) #맨위 좌측을 (0,0)으로 설정
apple_row, apple_col = input_row -1, input_col - 1
board[apple_row][apple_col] = 1
apple.append((apple_row, apple_col))

L = int(input()) #뱀의 회전정보 받기
change_snake = []
for _ in range(L): #방향 회전 정보를 리스트에 추가
    dis, direct = input().split()
    dis=int(dis)
    change_snake.append((dis, direct))

change_snake.append((10001, '')) #문제를 10000초 이하로 해결

change = [(0,1), (0,-1),(1,0),(-1,0)]

def turn
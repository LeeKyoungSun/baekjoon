from collections import deque

n, k = map(int, input().split())#입력된 문자열을 공백으로 split()하고, 각각의 요소를 int로 변환

# 1~n번 사람
people = deque() #사람의 번호를 저장할 deque
for i in range(1, n+1): people.append(i)
result = [] #제거된 사람들의 순서를 기록할 리스트

while people: #사람이 남아있을 때까지 실행
  for _ in range(k-1):
    people.append(people.popleft()) #popleft()는 큐의 맨 앞에 있는 사람을 제거하고 그 값을 반환
															     #제거된 사람은 다시 맨 뒤에 추가:append()

  result.append(people.popleft()) #큐의 맨 앞인 k번째 사람을 제거(popleft())하고, result에 추가

print(str(result).replace('[', '<').replace(']', '>')) #str(result): 리스트를 문자열로 변환
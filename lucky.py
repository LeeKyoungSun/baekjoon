n, k = map(int, input().split())
wheel = ['?'] * n #바퀴 초기화
idx = 0
check = True

for i in range(k):
    num, alphabet = input().split()
    idx = (idx + int(num)) % n #바퀴는 원형이므로 n으로 나누었을 때의 나머지를 idx로 설정
    if wheel[idx] != '?': #알파벳이 존재하는 경우
        if wheel[idx] == alphabet: #같은 알파벳이면 상관 X
            continue
        check = False #해당하는 바퀴가 없는 것으로 처리
    else:
        wheel[idx] = alphabet #위의 경우가 아니면 알파벳을 삽입

for i in range(n):
    if wheel[i] == '?': #'?'는 중복 가능
        continue
    for j in range(i + 1, n):
        if wheel[i] == wheel[j]: #중복된 값이 존재하는 경우
            check = False        #해당하는 행운의 바퀴가 없는 것으로 처리
            break

if check:
    for _ in range(n):
        print(wheel[idx], end='')
        idx = (idx - 1) % n
else:
    print('!')

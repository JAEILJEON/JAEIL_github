#문자열 뒤집기 복습
#정답~
'''
s = input()

count0 = 0 # 1에서 0
count1 = 0 # 0에서 1

if s[0] == '0':
    count1 += 1
else:
    count0 += 1

for i in range(len(s)-1):
    if s[i] != s[i+1]:
        if s[i] == '0':
            count1 += 1
        else:
            count0 += 1

print(min(count1, count0))
'''

#곱하기 혹은 더하기 복습
#정답~
'''
s = input()

result = int(s[0])

for i in range(1,len(s)):
    num = int(s[i])
    if result <= 1 or num <= 1:
        result = result + num
    else:
        result *= num

print(result)
'''

#모험가 길드
#정답~
'''
n = int(input())
data = list(map(int, input().split()))
data.sort()

count = 0
result = 0

for i in data:
    count += 1
    if i <= count:
        result += 1
        count = 0

print(result)
'''
#1이 될 때까지
# 틀렸다가 놓친 부분 겨우 찾았다.......
'''
n, k = map(int, input().split())

result = 0

while True:
    target = (n // k) * k
    result += (n - target)
    n = target
    if n < k:
        break
    n = n // k
    result += 1

result += (n-1)
print(result)
'''
#숫자 카드 게임
#정답~
'''
n, m = map(int, input().split())

min_v = 0
max_v = 0

for i in range(n):
    data = list(map(int,input().split()))
    min_v = min(data)
    max_v = max(min_v,max_v)

print(max_v)
'''
#큰 수의 법칙
#나는 바보라서 참 힘들게 이해했다.. 그래도 이해한 게 어디야!!! 칭찬해 스스로.
#공부 시작할 때마다 한번씩 다시 풀어보자.
# 오늘 2번 더, 내일 다른 문제들 복습할 때 또 같이
'''
n, m, k = map(int,input().split())
data = list(map(int,input().split()))
result = 0

data.sort(reverse = True)

print(data)

first = data[0]
second = data[1]

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1

print(result)
'''
#만들 수 없는 금액
# 진짜 아이디어부터 아예 이해못했었다. 간신히 풀었네.
# 얘는 진짜 계속 복습해야겠다.
'''
n = int(input())
data = list(map(int, input().split()))

data.sort()

target = 1

for i in data:
    if target < i:  #이 부분. 만들 수 없는 금액 나오는 경우는 2가지인데,
                    #i가 아예 target 보다 더 커버리는 경우
        break
    target = target + i     #요소들 다 더해도 타겟보다 작은 경우 - 요소들 다 출력되어보며 반복문 끝.

print(target)
'''
#구현 문제인데 지금 내 기초가 너무너무 부족하다 진짜!
#백준 기초 강의로 들어가서 독파해보자. 기초를 쌓고 독파해보자!
# N 입력받기 
n = int(input())
x, y = 1, 1
plans = input().split()

#L R U D에 따른 이동 방향
dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types = ['L','R','U','D']

#이동 계획을 하나씩 확인
for plan in plans:
    #이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    #공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    #이동 수행
    x, y = nx, ny

print(x, y)







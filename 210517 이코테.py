###그리디 - 큰 수의 법칙 ###
'''
#내가 풀고 맞은 것~
n, m, k = map(int, input().split())
d = list(map(int, input().split()))

d.sort(reverse = True)
print(d)

d1 = (m % k) * d[1]
d2 = (m - (m % k)) * d[0]
t = d1 + d2
print(t)
'''
###그리디 - 숫자 카드 게임 ###
'''
#내가 풀다 틀린 것
d = []

n, m = map(int, input().split())

#for i in range(n):
for j in range(m):       
    d1 = list(map(int,input().split()))
    d.append(d1)
print(d)

a = []
mi = d[0][0]

for i in range(n):
    for j in range(m):
        if mi > d[i][j]:
            mi = d[i][j]
    a.append(mi)
        
        
b = a.sort(reverse = True)
print(a)

#모범 답안 내가 풀어본 것 2중 for문 x
n, m = map(int,input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_v = min(data)
    result = max(min_v, result)
print(result)
'''
### 그리디 - 1 남을 때까지
'''
#내가 푼 건데 으악 모르겠어
n, k = map(int,input('입력해 : ').split())

x, y = 0, 0

while True:
    n = n - 1
    x = x + 1
    if n % k == 0:
        break

    while True:
        n = n // k
        y = y + 1
        if n == 1:
            break

print(x + y)

#모범답안

#n, k를 공백으로 구분하여 입력받기
n ,k = map(int, input().split())
result = 0

while True:
    #n == k로 나누어 떨어지는 수가 될 때까지 1씩 빼기
    target = (n // k) * k
    result = result + (n - target)
    n = target
    #(n이 k보다 작아서 더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    #k로 나누기
    result = result + 1
    n = n // k

#마지막으로 남은 수에 대하여 1씩 빼기
result = result + (n-1)
print(result)
'''
'''
#모범 답안 이해하고 내가 풀어낸 것.
#n, k 공백으로 입력 받고
n, k = map(int, input().split())
# 횟수 초기값 설정하고
result = 0

while True:
    # 타겟은 k로 나누어떨어지는 수까지 1씩 몇번 빼줄까를 위해 생성.
    target = (n // k) * k
    # n - 타겟으로 1씩 빼는 횟수를 설정함.
    result = result + (n - target)
    # n에 타겟 할당해서, k로 나누어떨어지는 수로 만든다. 아래서 횟수 1 추가하고 나눌 거라
    n = target
    #만약에 n이 k보다 작아서 더 이상 나눌 수 없으면 반복문 탈출
    if n < k:
        break
    #n이 k보다 아직 크면, k로 나누어떨어지게 하고 횟수 1 추가
    n = n // k
    result = result + 1
#반복문 빠져나온 뒤, 즉 n < k보다 작아서 1까지 마지막으로 1씩 빼주는 것만 남았을 때
#n - 1만큼 1씩 뺀 횟수 추가
result = result + (n -1)
print(result)
'''
### 11장 그리디 문제 01 모험가 길드
'''
#내가 고민했던 것
아이디어, 실험
n = 5

d = [1,2,2,2,3]

a = d[-1:d[
-n]:-1]
b = d[0:3:1]

print(a)
print(b)

#모범 답안 보고 푼 것
n = int(input())
data = list(map(int, input().split()))

#총 그룹 수
result = 0
#현 그룹 내 인원 수
count = 0
#data 오름차순 정렬
data.sort()

#data를 i로 넣어 반복
for i in data:
    count = count + 1 

    #만약 i, 공포도가 모험가 수와 같거나 많다면
    if i <= count:
        #총 그룹 +1
        result = result + 1
        # 현 그룹 내 인원 초기화
        count = 0

print(result)
'''
#숫자카드게임 복습
#성공
'''
n, m = map(int, input().split())

b = 0

for i in range(n): #층으로 반복
    data = list(map(int, input().split()))
    min_v = min(data)
    b = max(b, min_v)

print(b)
'''
# 1이 될 때까지 복습
# 성공이긴 한데 뭔가 기억에 남아있어서 푼 느낌. 완전히 이해하고 풀었는지는 물음표.
# 다시 공부해볼 것.
'''
n, k = map(int, input().split())

result = 0

while True:
    target = (n // k) * k
    result = result + (n - target)
    n = target
    if n < k:
        break
    n = n // k
    result = result + 1

result = result + (n - 1)
print(result)
'''
#모험가 길드 복습
# 성공.
#그래도 모든 문제들 5회차 될 때까지 복습이야.
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
'''
d = []
s = input()
count = 0

#print(len(s))

for i in range(len(s)):
    s[i:i]
    #d.append(s)
    #d.append(s[i])

print(s)
'''
### 11장 그리디 문제 02 곱하기 혹은 더하기
'''
#내 힘으로 온전히 스스로 고민해서 풀어냈다!!!!!!!!!!!!!!!!!
# 0518 내일 답지 보면서 복습해봐야지!
s = input()
c = []
count = 1 #카운트가 1이어도 아무 영향 못미침.
          #애초에 c[j]가 0이 아니면 곱하기 시작이고, c[j]가 0이면 더해봤자 1 그대로.
          #1그대로고, 곱하기 시작이니까 c[j] 곱한 거 그대로 들어가면서 시작됨.
          # count가 1이어야 애초에 시작이 가능함. 어짜피 곱하기부터 시작되니까.


          
# 드디어 문자열 슬라이싱해서 반복문으로 넣기 성공했다. 정수로 변환까지.
for i in range(len(s)):
    c.append(int(s[i:i+1]))

for j in range(len(c)):
    if c[j] == 0:
        count = count + c[j]
    else:
        count = count * c[j]
print(count)
'''






























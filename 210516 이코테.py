###그리디 - 거스름돈 예제###
'''
#내가 풀고 맞은 것
n = int(input())

a = n // 500
a1 = n % 500

b = a1 // 100
b1 = a1 % 100

c = b1 // 50
c1 = b1 % 50

d = c1 // 10

m = (a+b+c+d)

print(m)
'''
#모범 답안
'''
n = int(input())
count = 0

coin_types = [500,100,50,10]

for coin in coin_types:
    count = count + (n // coin)
    n = n % coin

print(count)
'''
#모범 답안대로 스스로 짜본 것
'''
n = 1260
count = 0

coin_types = [500,100,50,10]

for coin in coin_types:
    count = count + (n // coin)
    n = n % coin

print(count)
'''
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

n = 5

d = [1,2,2,2,3]

a = d[-1:d[-n]:-1]
b = d[0:3:1]

print(a)
print(b)

















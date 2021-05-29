#큰 수의 법칙
#간만에 풀었는데 정답~
'''
n, m, k = map(int, input().split())
arr = list(map(int, input().split()))


result = 0

arr.sort(reverse = True)

big1 = arr[0]
big2 = arr[1]

while m > 0:
    for i in range(k):
        result += big1
        m -= 1
    result += big2
    m -= 1

print(result)
'''

#숫자 카드 게임
#간만에 풀었는데 정답~
'''
n, m = map(int, input().split())

li = []

result = 0

for i in range(n):
    data1 = list(map(int, input().split()))
    li.append(min(data1))

result = max(li)

print(result)
'''
#1이 될 때까지
#간만에 풀었는데 정답~
'''
n, k = map(int, input().split())
result = 0

while True:
    target = (n//k) * k
    result = result + n - target
    n = target
    if n < k:
        break
    n = n // k
    result += 1

result = result + (n -1)
print(result)
'''
#모험가 길드
#간만에 풀었는데 정답~
'''
n = int(input())
x = list(map(int, input().split()))

x.sort()

result = 0
count = 0

for i in x:
    count += 1
    if count == i:
        result += 1
        count = 0

print(result)
'''
#곱하기 혹은 더하기
#간만에 풀었는데 정답~
'''
n = input()
num = []
count = 1

for i in n:
    num.append(int(i))

for j in range(len(num)):
    if num[j] != 0 and num[j] != 1:
        count *= num[j]
    else:
        count += num[j]

print(count)
'''
#문자열 뒤집기
#간만에 풀었는데 정답~
'''
s = input()
data0 = 0
data1 = 0

if s[0] == '1':
    data1 += 1
elif s[0] == '1':
    data0 += 1

for i in range(1, len(s)-1):
    if s[i] != s[i+1]:
        if s[i] == '0':
            data0 += 1
        elif s[i] == '1':
            data1 += 1

print(min(data1, data0))
'''
# 코드업 6092
# 이것도 맞혔다. 실력이 늘긴 했군!
'''
n = int(input())
li = list(map(int, input().split()))

count = []

for i in range(23):
    count.append(0)

for j in li:
    count[j-1] += 1

for x in count:
    print(x, end = ' ')
'''
# 코드업 6094
# 음 너무 쉽고..
'''
n = int(input())
li = list(map(int, input().split()))
count = []

for i in li:
    count.append(i)

print(min(count))
'''
# 코드업 6096

n  = int(input()) # 몇번 실행할 건지
count = []

for i in range(19):
    count.append([])
    for j in range(19):
        count[i].append(0)

for i in range(n):
    x, y = map(int, input().split())

for i in range(19):
    count[i][y-1] = 1
    for j in range(19):
        count[x-1][i] = 1

    
for i in range(19):
    for j in range(19):
        print(count[i][j
                       ], end = ' ')
    print()


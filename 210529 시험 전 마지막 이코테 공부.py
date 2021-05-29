'''
n,m,k = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort(reverse = True)
result = 0

while True:
    if m <= 0:
        break
    
    for i in range(k):
        result += arr[0]
        m -= 1
    if m < 0:
        break
    result += arr[1]
    m -= 1

print(result)
'''
'''
n, m = map(int, input().split())
d = []

for i in range(n):
    x = map(int, input().split())
    d.append(min(x))

print(max(d))
'''
'''
n, k = map(int, input().split())
result = 0

while True:
    target = (n//k)*k
    result += n - target
    n = target

    if n < k:
        break

    n = n//k
    result += 1

result += (n-1)
print(result)
'''
'''
n = int(input())
x = list(map(int, input().split()))
result = 0
count = 0

x.sort()

for i in x:
    count += 1
    if count == i:
        result += 1
        count = 0

print(result)
'''
'''
d = []
s = input()
count = 1

for i in s:
    d.append(int(i))

for j in range(len(d)):
    if d[j] == 0 and d[j] == 1:
        count += d[j]
    else:
        count *= d[j]

print(count)
'''
'''
s = input()
data0 = 0
data1 = 0

if s[0] == '0':
    data0 += 1
elif s[0] == '1':
    data1 += 1

for i in range(1,len(s)-1):
    if s[i] != s[i+1]:
        if s[i] == '0':
            data0 += 1
        elif s[i] == '1':
            data1 += 1

print(min(data0, data1))
'''

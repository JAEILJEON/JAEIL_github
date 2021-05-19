# 숫자카드게임 복습
'''
# 처음엔 틀렸으나 고쳐서 해결.
n, m = map(int, input().split())

#min_v = 0
max_v = 0

for i in range(n):
    data = list(map(int, input().split()))

    min_v = min(data)
    max_v = max(min_v, max_v)

print(max_v)
'''
#1이 될 때까지 복습
'''
#정답~
n, k = map(int, input().split())
result = 0

while True:
    target = (n//k) * k
    result = result + (n - target)

    n = target

    if n < k:
        break
    n = (n // k)
    result = result + 1

result = result + (n - 1)
print(result)
'''
#모험가 길드 복습
'''
#정답~
n = int(input())

data = list(map(int, input().split()))
data.sort()

count = 0
result = 0

for i in data:
    count = count + 1
    if count >= i:
        result = result + 1
        count = 0

print(result)
'''
#곱하기 혹은 더하기 복습
'''
#정답~
d = []
s = input()

count = 1

for i in range(1,len(s)+1):
    d.append(int(s[i-1:i]))

#print(d)
for i in range(len(d)):
    if d[i] == 0:
        count = count + d[i]
    elif d[i] == 1:
        count = count - 1
        count = count + d[i]
    else:
        count = count * d[i]
print(count)
'''
# s에 숫자를 문자열로 입력 받고 각 요소별로 슬라이싱해서 정수형으로 리스트에 append 시키는 법.
# 내가 짜낸 방법
'''
d = []
s = input()

for i in range(1,len(s)+1):
    d.append(int(s[i-1:i]))
'''
# 곱하기 더하기 모범 답안 한번 보자.
# 정답~ 이긴 하지만 2수만 갖고 비교하는 이게 훨씬 간단해보여. 다음 복습 땐 이렇게 풀어보자.
'''
data = input()

result = int(data[0])

for i in range(1,len(data)):
    num = int(data[i])

    if num <= 1 or result <= 1:
        result = result + num
    else:
        result = result * num

print(result)
'''
#문자열 뒤집기
'''
#내가 푼 건데, 뭔가 아이디어는 잡은 것 같은데 '연속 되는지 확인하는 것'을 풀어내지 못했다.
s = input()
count = 0
result1 = 0
result2 = 0


for i in range(1,len(s)):
    if s[i-1] == '0' and s[i-1] == s[i]:
        count += 1
    else:
        result1 = result1 + 1
        count = 0
        
    if s[i] == '1':
        count += 1
    else:
        result2 = result2 + 1
        count = 0

print(result1)
print(result2)
#result = min(result1, result2)
#print(result)
'''
#문자열 뒤집기
#드디어 모범답안을 이해하고 겨우 풀었다...!!!!!!1
#밥 먹고 와서 한번 더 풀자. 이 책에서 한 것 중 가장 어려웠음 지금까지 ㅠ
'''
s = input()

count0 = 0 # 0 -> 1 변화
count1 = 0 # 1 -> 0 변화

# 첫번째 요소부터 확인
if s[0] == '1':
    count1 += 1
else:
    count0 += 1

# 두번째 요소부터 쭉 확인
for i in range(len(s)- 1): #-1하는 이유는, 첫번째 요소를 이미 파악해서 2번째부터 파악하니까 횟수 하나 줄여줌.
    if s[i] != s[i+1]: #s[i]번째와 i+1번째와 다르다면,
        if s[i] == '1':  #다른데 1이라면, 1에서 0으로 바뀌어야하니까
            count0 += 1
        else:
            count1 += 1
            
print(min(count0, count1))
'''
#밥 먹고 와서 한번 더 풀어보자. 이건 머리에 남아있을 때 한번 더 푼 거고.
'''
s = input()

count0 = 0 #0을 1로 바꾸며 체크
count1 = 0 #1을 0으로 바꾸며 체크

#첫번째 요소부터 확인
if s[0] == '1':
    count1 += 1
else:
    count0 += 1

#두번째 요소부터 쭉 확인
for i in range(len(s)-1): #여기서 -1 하는 이유는, 이미 첫번째에 한개를 체크했잖아
    if s[i] != s[i+1]: #만약 i와 i+1번이 다르면...!!(바뀌는 게 체크되며 +1되는 순간)
        if s[i] == '1':
            count1 += 1
        else:
            count0 += 1

print(min(count1, count0))
'''
#밥 먹고 와서 한번 더 풀어본 것.
#거의 한 5번 6번 풀어본 것 같다. 어쨌든 다음에 또 풀어볼 거임.
'''
s = input()

count0 = 0 #1 -> 0로 바뀌는 것
count1 = 0 #0 -> 1로 바뀌는 것

#0번째 요소 먼저 체크
if s[0] == '0':
    count1 += 1
else:
    count0 += 1

#1번째 요소부터 이어서 체크
for i in range(len(s)-1): #-1하는 이유는 => 이미 0번째 요소를 체크했기 때문에 횟수 -1임.
    if s[i] != s[i+1]:  #s[i] != s[i+1]의 의미는 바뀌는 순간이라는 것. 바뀐다 == 체크해야함. 
        if s[i] == '1':
            count0 += 1
        else:
            count1 += 1

print(min(count0, count1))
'''
















#최대공약수(GCD) 구하기.
'''
#유클리드 호제법
a % b = r
GCD(a,b) = GCD(b,r)
재귀 함수와 반복문을 통해서도 구할 수 있음.
GCD(a,b,c) = GCD(GCD(a,b),c) 이렇게 3개, N개의 숫자도 같은 방식으로 구할 수 있다.
'''
#최소공배수(LCM)
'''
G = GCD(a,b) LCM(a,b) = G * a/G * b/G

2609
최대공약수와 최소공배수 문제

#재귀함수로
def = gcd(x,y):
    if y == 0:
        return x:
    else:
        return gcd(y,x%y)
a,b = map(int, input().split())
g = gcd(a,b)
print(g)
print(a*b // g)
'''

#소수
'''
약수가 1과 자기 자신 밖에 없는 수 = n이 2~(n-1)까지 나누어 떨어지지 않으면 소수

소수 구하는 2가지 방법
굳이 나는 이유는, 1번을 n번 하는 것보다 더 빠른 알고리즘이 있기 때문.

1. 어떤 수 n이 소수인지 아닌지
- 소수의 정의를 그대로 이용. n이 2~(n-1)까지 나누어 떨어지지 않으면 되니까 진짜 해보면 돼.
시간 복잡도 O(n)


2. n 이하의 모든 소수를 구하기
- 약수의 특징을 이용. 1과 n이 아닌 약수 중에서 가장 작은 약수 찾기.
ex) 만약 가장 작은 약수가 2가 되면, 모든 약수는 루트2로 대칭을 이룬다.
만약 2가 가장 작은 약수가 2면, 대칭을 이루는 n/2는 가장 큰 약수가 되는 것.
n/2 + 1 부터 n-1까지 있는 수 중에는 절대 약수가 없다.
2~n/2까지 나누어 떨어지면 되는지 보면 되는 거야. 이것 또한 복잡도는 o(n).

더 빠른 방법이 필요한데, 이는 2부터 루트 n까지 나누어 떨어지는지 검사해보는 것.o(루트 n)
이게 가장 빠른 방법. 그 이유는, 모든 약수는 루트 n을 기준으로 그거와 곱해져서 n을 만드는
수가 무조건 존재. 루트 n보다 작거나 같은 쪽만 검사를 해줘도, 대칭 쪽을 굳이 검사할 필요 없음.

이건 최대한 정수만 찾는 것이 좋음. 실수는 근삿값이니까.

루트 n 판별법을 어떻게 코드로 구현했는가?

코드
1번 방식 -> 시간 복잡도 o(루트 n)
def is_prime(x):
    if x < 2:
        return False
    i = 2   # 2부터 시작하고, i+1씩 해서 i**2가 x보다 작거나 같은 동안 true리턴으로 소수인지 아닌지 판별.
    while i * i <= x:    #파이썬에서 for는 제곱보다 같거나 작다는 걸 할 수 없어서 while 썼다.
        if x % i == 0:
            return False
        i += 1
    return True

n = int(input())
a = list(map(int, input().split()))
ans = 0
for x in a:
    if is_prime(x):
        ans += 1
print(ans)

2번 방식 -> 시간복잡도 = 1번 방식을 n번 하면 돼. o(n*루트n)
2번을 별도로 알아보는 방법은, 더 빠른 방법이 있기 떄문.
바로 '에라토스테네스의 체' 오우씨 ㅋㅋㅋㅋㅋ이거 이제 알았네 ㅋㅋㅋㅋ

#####에라토스테네스의 체#####
1) 2부터 n까지 모든 수를 써놓는다.
2) 아직 지워지지 않은 수 중에서 가장 작은 수를 찾는다.
3) 그 수는 소수이다.
4) 이제 그 수의 배수를 모두 지운다.

- 예시에 10 * 10 박스에서 지우는 걸 봤는데, 2 3 5 7 이상 부터는 각 수의 제곱들만 지우면 돼.

이를 위해선 2개의 배열이 필요한데, 리스트로 실제로 수를 지우면 그 지우는데도 시간이 필요.

1) 수를 지웠는지 아닌지
    지움: True
    지우지 않음 : False

2) 소수의 목록을 유지

1929
MAX = 1000000
check = [0]*(MAX + 1)
check[0] = check[1] = True   #배열 만들어 주고, True는 지워짐을 의미.

for i in range(2, MAX + 1):
    if not check[i]:         #지워지지 않은 경우(False)에만 i씩 증가해가며 1씩 지운다.
        j = i+1
        while j <= MAX:
            check[j] = True
            j += i
            
m,n = map(int,input().split())
for i in range(m, n + 1):   # 지워지지 않았다면 소수라고 할 수 있으니 출력.
    if check[i] == False:
        print(i)


#####골드 바흐의 추측#####
증명이 되어있지 않기 때문에 추측임. 하지만 10**18 이하에서는 참인 것이 증명됨.
1) 2보다 큰 모든 짝수는 두 소수의 합으로 표현 가능.
2) 1)의 문장에 3을 더하면
3) 5보다 큰 모든 홀수는 세 소수의 합으로 표현 가능하다.
1번 문장이 3번 문장으로 바뀐다!

6588
골드바흐의 추측 문제 - 백만 이하의 짝수에 대해 골드 바흐의 추측을 검증하는 것.
백만 이하의 짝수가 입력으로 들어왔을 때 두 소수의 합으로 표현 가능한지 알아보는 것.

MAX = 1000000
check = [0] * (MAX + 1)
check[0] = check[1] = True
prime =[]                     #prime 여기에 소수를 다 넣을 거고,
for i in range(2, MAX + 1)    # 5번부터 11번 라인까지 에나토스테네스의 체 구현완료.
    if not check[i]:          #지워지지 않았으면
        prime.append(i)       #소수에다가 i를 넣어주고.
        j = i+i               #모든 i의 배수를 지워준다.
        while j <= MAX:       
            check[j] = True
            j += i
prime = prime[i:]           #파이썬 소스 코드는 아예 2를 지워주고 시작.
while True:                   
    n = int(input())
    if n == 0:
        break
    for p in prime:           # a+b=n인데, n이 a와 b 두소수의 합으로 표현되는지 궁금하잖아.
        if check[n-p] == False:     #a가 p인 건 당연하고(a는 소수가 저장된 곳에서 가져왔으니까),  
            print('{0} = {1} + {2}'.format(n, p, n-p))    #n-p가 소수인지만 검사하면 돼. 체에서 지워지지 않았는지만 확인하면 돼.
            break

소수 문제에선 거의 다 에라토스테네스의 체로 해결 가능! 


 

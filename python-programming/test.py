#a,b,c,d = map(int, (input().split()))
t = []
n = input()
for i in range(n):
    t.append(int(input()))

def gcd(a,b):
    if b > a:
        a = b
        b = a
    while b == 1:
        a = b
        b = a % b
        if b == 1:
            return a


ans = t[0]
for i in range(1, n):
    ans = ans * t[i] // gcd(ans, t[i])
print(ans)



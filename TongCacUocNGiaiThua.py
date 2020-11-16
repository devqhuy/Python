'''def analyze(n):
    k=[]
    i=2
    while i*i<=n:
        dem=0
        while n%i==0:
            dem+=1
            n//i #chia nguyen
        if dem!=0: k.append((i,dem))
        i+=1
    if n>1: k.append((n,1))
    return k

def divide_count(n):
    p = [0] * (n + 1)  # mang n+1 gia tri 0
    for i in range(2, n + 1):
        for u,v in analyze(i): p[u]+=v
    d,s=1,1
    for i in range(2,n+1):
        if p[i]:
            d*=(p[i]+1)
            s*=(i**(p[i]+1)-1)//(i-1)
    return d,s

if __name__ == '__main__':
    n = int(input("nhap n = "))
    d,s = divide_count(n)
    print("so uoc",d)
    print("tong uoc",s)
'''
def POW(x,n):
    if n==0:return 1
    return POW(x*x,n//2)*(x if n%2 else 1)
def Fib(n):
    return 1 if n<=1 else (Fib(n-1)+Fib(n-2))
def FibAd(n):
    if n==0: return 1,1
    u,v=FibAd(n-1)
    return v,u+v
def FibAd2(n):
    if n==0: return (1,0)
    if n==1: return(1,1)
    a,b = FibAd2(n//2)
    a,b = a*b+b*b,2*a*a-b*b
    return (a+b,a) if n%2 else (a,b)
if __name__ == '__main__':
    for n in range(1000000):
        u,v=FibAd2(n)
        print(n,v)



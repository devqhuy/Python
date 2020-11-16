def exp(n,x):
    p,s=1,1
    for i in range(1,n+1,1):
        p = p*x/i
        s=s+p
    return s
"""
if __name__ == '__main__':
    n = int(input("nhap n = "))
    x = float(input("nhap x = "))
    print(exp(n,x))
  """
if __name__ == '__main__':
    n = int(input())
    s = 0
    r = range(1,n+1)
    for i,j in zip(r,r[::-1]): s+=i/j;
    print("gia tri", s)
    
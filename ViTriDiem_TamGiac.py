from collections import namedtuple
from math import fabs
Diem = namedtuple("Diem", "x,y")
def dt(A,B,C):
    return fabs((A.x * B.y - A.y * B.x) + (B.x * C.y - B.y * C.x) + (C.x * A.y - C.y * A.x))
if __name__ == '__main__':
    u, v = map(float, input().split())
    A= Diem(u,v)
    u, v = map(float, input().split())
    B = Diem(u, v)
    u, v = map(float, input().split())
    C = Diem(u, v)
    u, v = map(float, input().split())
    M = Diem(u, v)
    s,s1,s2,s3=dt(A,B,C),dt(A,B,M),dt(B,C,M),dt(C,A,M)

    if s == s1+s2+s3: print("tren" if s1*s2*s3==0 else "trong")
    else: print("ngoai")

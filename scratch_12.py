"""if __name__ == '__main__':
    b = [x for x in range(1,20,2)]
    print("5 phan tu dau la " , b[:5])
    print("ba phan tu cuoi ",b[-3:])
    print("hai phan tu cuoi ",b[-1],b[-2])
    print("nhung phan tu vi tri chan ",b[::2])
    b.append(4)
    b.append(4)
    print(b)
    b.remove(4)
    print(b)

    c=[x for x in b if x!=5]
    print("danh sách khác 5 là ",c)
    d = list(filter(lambda  x:x!=5,b))
    print("danh sach d: ",d)

    a = [1,2,3]+[4,5,6,9,7]
    print(a)"""""
from functools import reduce
from math import gcd as ucln
if __name__ == '__main__':
    n=int(input())
    print(reduce(lambda x,y:x*y, range(1,n+1)))
    d = [120,240,180,144]
    print("ucln day", reduce(ucln,d))
    e = list(map(lambda x:x%13,d))
    print(e)
'''
#BUPBETHAMLAM
from queue import Queue

if __name__ == '__main__':
    k, *a = [int(x) for x in input().split()]
    a.sort(reverse=True)
    Q = Queue()
    res = 0
    for x in a:
        if Q.qsize() and Q.queue[0] >= k + x:
            Q.get()
        else:
            res += x
        Q.put(x)
    print("so bup be = ", Q.qsize())
    print("dien tich nho nhat cat giu tat ca bup be = ", res)
'''



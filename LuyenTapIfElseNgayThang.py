def nhuan(y): return y%400==0 or (y%4==0 and y%100)
if __name__ == '__main__':
    d,m,y=map(int,input().split('/'))
    t=[0,31,28+int(nhuan(y)),31,30,31,30,31,31,30,31,30,31]
    if d==t[m]:
        d=1
        m=m+1
        if m==13: m,y=1,y+1
    else:
        d=d+1
    print("{0:d}/{1:d}/{2:d}".format(d,m,y))
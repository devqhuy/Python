''' global dem = 0
def TRY(x,k,T,n,M,dem):
    if k == n-1:
        x.append(M-T)
        dem = dem +1
        print(dem,M," = ")
        print(*x,sep="+")
    else:
        for t in range(M-T+1): TRY(x+[t], k+1, T+t,n,M,dem+1)

if __name__ == '__main__':
    TRY([],0,0,3,5'''
import self as self


class money:
    def nhap(self):
        self.a = list(map(int, input().split()))
        self.M=int(input())
        self.n=len(self.a)
    def TRY(self,x,k,T):
        if len(x) == self.n-1:
            if(self.M - T)%self.a[-1]==0:
                t=(self.M-T)//self.a[-1]
                print(*(x+[t]),sep = " ")
            else:
                for t in range((self.M - T)// self.a[k]+1):self.TRY(x+[t],k+1,T+t*self.a[k])

    def sol(self):
        self.nhap()
        self.TRY([],0,0)

if __name__ == '__main__':
    mon = money()
    mon.sol()

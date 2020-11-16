import numpy
class ocSen:
    m = numpy.array()
    def __init__(self,fname):
        f=open(fname,"r")
        for line in f.read().split("\n"):
            a=list(map(int,line.split()))
            self.m.append(a)
        f.close()
        n=len(self.m[0])
        m=[1]*n+self.m+[1]*n
    def dfs(self,u,v):
        self.m[u][v]=1
        self.count+=1
        hh=[1,-1,0,0]
        hc=[0,0,1,-1]
        for z,t in zip(hh,hc):
            if self.m[u+z][v+t]==0: self.dfs(u+z,v+t)
    def sol(self):
        u,v=map(int,input("toa do oc sen: ").split())
        self.dfs(u,v)
        print("so o di duoc: ",self.count)
if __name__ == '__main__':
    O = ocSen("ocsen.txt")
    O = ocSen.sol()
from math import gcd
class fraction:
    def __init__(self,a=0,b=1):
        d=gcd(a,b)
        if b<0: a,b=-a,-b
        self.tu=a//b
        self.mai=b//d


    def __str__(self):
        return str(self.tu)+"/"+str(self.mau)
    def __mul__(self, other):
        u=self.tu*other.mau+self.mau*other.tu
        v=self.mau*other.mau
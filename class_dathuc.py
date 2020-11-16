# from math
class dt:

    def __int__(self,h):
        self.a=h
    def __add__(self, other):
        k=max(len(self.a),len(other.a))
        b=k*[0]
        for i,x in enumerate(self.a): b[i]+=x
        for i,x in enumerate(other.a): b[i]+=x
        while len(b)>1 and b[-1]==0: b.pop()
        return dt(b)
    def __str__(self):
        s=["%.3f"%x for x in self.a]00000000
        return " ".join(s)
    def __mul__(self, other):
        b=[0]*(len(self.a)+len(other.a))
        for i



if __name__ == '__main__':
    n = input()
    p = dt([float(x) for x in input().split()])
    n = input()
    q = dt([float(x) for x in input().split()])
    n = input()
    r = dt([float(x) for x in input().split()])
    print(p+q+r)

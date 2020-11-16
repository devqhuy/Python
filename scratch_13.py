if __name__ == '__main__':
    n = input()
    a =list(map(int,input().split()))
    for k in range (3):
        b=list(filter(lambda x:x%3==k,a))
        if b: print(min(b),max(b))
        else: print("Khong co so nao chia 3 du",k)
if __name__ == '__main__': 
    a=int(input('nhap a = ')) 
    b=int(input('nhap b = ')) 
    while a!=b: 
        if a>b: a=a-b 
        else: b=b-a 
    print("uoc chung lon nhat {0:d}".format(a))
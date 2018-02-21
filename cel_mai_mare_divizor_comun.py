def cmmdc(a,b):
    r = a%b
    if r==0:
        return b
    elif r==1:
        return 1
    print(b)
    return cmmdc(b,r)
if __name__ == '__main__':
    print(cmmdc(216,28))

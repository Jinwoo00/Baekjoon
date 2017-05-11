def gcd_func(a, b):
    mod = a%b

    while mod>0:
        a=b
        b=mod
        mod=a%b

    return b;
    

n=input()
n=n.split(":")

gcd=gcd_func(int(n[0]),int(n[1]))

print(str(int(int(n[0])/gcd))+":"+str(int(int(n[1])/gcd)))

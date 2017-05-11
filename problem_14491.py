n=int(input())
result=[]
quo=int(n/9)
rem=n%9
result.append(rem)

while quo!=0:    
    rem=quo%9
    result.append(rem)
    quo=int(quo/9)

i=len(result)
while i>0:
    print(result[i-1],end='')
    i-=1
    

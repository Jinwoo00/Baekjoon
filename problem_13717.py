N=int(input())

P=[]
C=[]

S=0
i=0
while i<2*N:
    if S==0:
        P.append(input())
        S=1
    elif S==1:
        K_M=input()
        K_M=K_M.split()
        C.append(K_M)
        S=0
    i+=1

sum=0
result=[]

j=0
while j<N:
    count=0
    K=int(C[j][0])
    M=int(C[j][1])
    
    while K<=M:
        M-=K
        M+=2
        count+=1

    sum+=count
    result.append(count)
    j+=1

print(sum)
print(P[result.index(max(result))])

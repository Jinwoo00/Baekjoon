N=input()
A=input()
B_C=input()

A=A.split()
B_C=B_C.split()

B=int(B_C[0])
C=int(B_C[1])

total=0
i=0
while i<len(A):
    if int(A[i])>B:
        temp=int(A[i])-B

        C_count=int(temp/C)
   
        if temp%C!=0:
            if temp%C>C:
                C_count+=2
            elif temp%C<C:
                C_count+=1
    
        total+=C_count+1
    elif int(A[i])<=B:
        total+=1
    i+=1

print(total)

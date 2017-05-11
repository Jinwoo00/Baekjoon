N=int(input())

A=input()
A=A.split(" ")
B=input()
B=B.split(" ")

i=0
while i<N:
    A[i]=int(A[i])
    B[i]=int(B[i])
    i+=1

A.sort()
B.sort(reverse=True)

S=0
for i in range(0, len(A)):
    S+=A[i]*B[i]

print(S)

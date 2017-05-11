def swap_func(array, a, b):
    tmp=array[a]
    array[a]=array[b]
    array[b]=tmp
    return array

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

A_tmp=A[:]
B_tmp=B[:]

j=0
while j<len(A_tmp)/2:
    max_a_index=A.index(max(A_tmp))
    min_b_index=B.index(min(B_tmp))

    A=swap_func(A, max_a_index, min_b_index)
    #print(A)
    
    min_a_index=A.index(min(A_tmp))
    max_b_index=B.index(max(B_tmp))

    A=swap_func(A, min_a_index, max_b_index)
    #print(A)
    
    del A_tmp[A_tmp.index(max(A_tmp))]
    del B_tmp[B_tmp.index(min(B_tmp))]
    del A_tmp[A_tmp.index(min(A_tmp))]
    del B_tmp[B_tmp.index(max(B_tmp))]    
    j+=1
    
S=0
for i in range(0, len(A)):
    S+=A[i]*B[i]

print(S)

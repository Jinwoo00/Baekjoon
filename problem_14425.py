NM=input()
NM=NM.split()

N_arr=[]
M_arr=[]

i=0
while i<int(NM[0]):
    N_arr.append(input())
    i+=1

j=0
while j<int(NM[1]):
    M_arr.append(input())
    j+=1

count=0
for x in range(0, len(M_arr)):
    if M_arr[x] in N_arr:
        count+=1

print(count)

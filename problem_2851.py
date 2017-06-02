arr=[]
sum_arr=[]

for i in range(0, 10):
    arr.append(int(input()))

sum=0
for j in range(0, 10):
    sum+=arr[j]
    sum_arr.append(sum)

index=0
min=abs(100-sum_arr[0])
for x in range(1, 10):
    if min > abs(100-sum_arr[x]) or min==abs(100-sum_arr[x]):
        index=x
        min=100-sum_arr[x]
               
print(sum_arr[index])

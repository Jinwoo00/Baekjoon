N=int(input())

arr=[]
x=0
while x<N:
    arr.append(int(input()))
    x+=1

for i in range(0, N):
    change=0
    for j in range(0, N-1):
        if arr[j]>arr[j+1]:
            change=1
            temp=arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=temp
    if change==0:
        break

print(i+1)

arr=[]
i=0
while i<5:
    arr.append(input())
    i+=1

j=0
maxarr=[]
while j<5:
    maxarr.append(len(arr[j]))
    j+=1
    
m=max(maxarr)

for x in range(0, m):
    for y in range(0, 5):
        if x<=len(arr[y])-1:
            print(arr[y][x],end='')

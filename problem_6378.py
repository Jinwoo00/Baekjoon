def func_sum(num):
    s=0
    x=0
    while x<len(num):
        s+=int(num[x])
        x+=1
    return str(s)

arr=[]
result=[]

tmp=''
i=0
while i<1000:
    arr.append(input())
    if arr[i]=='0':
        break
    i+=1

for j in range(0, len(arr)):
    if len(arr[j])>=2:
        tmp=func_sum(arr[j])
        #print(tmp)
        while len(tmp)!=1:
            tmp=func_sum(tmp)
           # print(tmp)
        print(tmp)

    elif arr[j]!='0':
        print(arr[j])

            

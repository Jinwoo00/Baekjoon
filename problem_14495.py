#def func(n):
#    result=0
#    if n==1 or n==2 or n==3:
#        return 1
#    else:
#        return func(n-1)+func(n-3)

    
n=int(input())
arr=[1,1,1]

if n>4:    
    i=3
    while i<n:
        arr.append(arr[i-1]+arr[i-3])
        i+=1

print(arr[n-1])

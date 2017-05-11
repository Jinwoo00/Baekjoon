def index_change(arr):
    change_arr=[]
    
    change_arr.append(max(arr))
    change_arr.append(min(arr))
    del arr[arr.index(max(arr))]
    del arr[arr.index(min(arr))]

    s=1
    while len(arr)!=0:
        if s==1:
            if len(arr)==1:
                if abs(change_arr[0]-arr[0])>abs(change_arr[len(change_arr)-1]-arr[0]):
                    change_arr.insert(0, arr[0])
                    break
                else:
                    change_arr.append(arr[0])
                    break
                
            change_arr.append(max(arr))
            change_arr.insert(0, min(arr))
            del arr[arr.index(max(arr))]
            del arr[arr.index(min(arr))]
            s=-1
                       
        elif s==-1:
            if len(arr)==1:
                if abs(change_arr[0]-arr[0])>abs(change_arr[len(change_arr)-1]-arr[0]):
                    change_arr.insert(0, arr[0])
                    break
                else:
                    change_arr.append(arr[0])
                    break

            change_arr.append(min(arr))
            change_arr.insert(0, max(arr))
            del arr[arr.index(max(arr))]
            del arr[arr.index(min(arr))]
            s=1
            
    return change_arr
    

n=int(input())
arr=input()

arr=arr.split()
i=0
while i<n:
    arr[i]=int(arr[i])
    i+=1

arr.sort()
arr=index_change(arr)
#print(arr)

result=0
j=0
while j<len(arr)-1:
    result+=abs(arr[j]-arr[j+1])
    j+=1
print(result)

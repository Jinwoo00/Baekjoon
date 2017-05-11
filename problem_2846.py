n=int(input())
numbers=input()
numbers=numbers.split()

i=0
while i<n:
    numbers[i]=int(numbers[i])
    i+=1

ascent=[]

j=0
start=numbers[0]

while j<len(numbers)-1:
    if numbers[j]>=numbers[j+1]:
        start=numbers[j+1]
    elif numbers[j]<numbers[j+1]:
        last=numbers[j+1]
        ascent.append(last-start)
    j+=1
    
ascent.sort()
#print(ascent)
if len(ascent)!=0:
    print(ascent[len(ascent)-1])
elif len(ascent)==0:
    print(0)

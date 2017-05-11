def self_number(num):
    first_n = num
    result=first_n
    num=str(num)
    i=0
    while i<len(num):
        result=result+int(num[i])
        i+=1
    return result

    
selfnumber=set([])
i=1
while i<=10000:
    selfnumber.add(i)
    i+=1


number=set([])
j=1
while j<=10000:
    x = self_number(j)
    if x<=10000:
        number.add(x)
    j+=1

selfnumber_list=list(selfnumber-number)
selfnumber_list.sort()
for x in selfnumber_list:
    print(x)

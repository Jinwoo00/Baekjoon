def right_number(number):
    if len(number)==2:
        return number[1]
    else:
        return number[0]
    

N=input()
count=1

if len(N)==1:
    N="0"+N[0]
    add_result=int(N[0])+int(N[1])#int
    new_number=N[1]+right_number(str(add_result))#string

    while N!=new_number:
        add_result=int(new_number[0])+int(new_number[1])
        add_result=str(add_result)
        new_number=new_number[1]+right_number(add_result)
        #print(new_number)
        count+=1

    print(count)
    

else:
    add_result=int(N[0])+int(N[1])#int
    new_number=N[1]+right_number(str(add_result))#string
    #print(new_number)

    while N!=new_number:
        add_result=int(new_number[0])+int(new_number[1])
        add_result=str(add_result)
        new_number=new_number[1]+right_number(add_result)
 #       print(new_number)
        count+=1

    print(count)




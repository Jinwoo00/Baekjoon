n=input()

number=[]
i=0
while i<len(n):
    if n[i]=="A" or n[i]=="B" or n[i]=="C":
        number.append(3)
    elif n[i]=="D" or n[i]=="E" or n[i]=="F":
        number.append(4)
    elif n[i]=="G" or n[i]=="H" or n[i]=="I":
        number.append(5)
    elif n[i]=="J" or n[i]=="K" or n[i]=="L":
        number.append(6)
    elif n[i]=="M" or n[i]=="N" or n[i]=="O":
        number.append(7)
    elif n[i]=="P" or n[i]=="Q" or n[i]=="R" or n[i]=="S":
        number.append(8)
    elif n[i]=="T" or n[i]=="U" or n[i]=="V":
        number.append(9)
    elif n[i]=="W" or n[i]=="X" or n[i]=="Y" or n[i]=="Z":
        number.append(10)
    i+=1

sum=0
for i in number:
    sum+=i

print(sum)

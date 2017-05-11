string=input()
string=string.split(" ")
sum=int(string[2])-int(string[1])
before=sum
    
for i in range(1, len(string)-1):
    after=int(string[i+1])-int(string[i])
    if before!=after:
        print("mixed")
        break

if before==after and int(string[0])<int(string[1]):
    print("ascending")
elif before==after and int(string[0])>int(string[1]):
    print("descending")
    
    

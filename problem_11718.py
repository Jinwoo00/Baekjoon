S=input()
count=0

S=S.split(' ')

for i in range(0, len(S)):
    if len(S[i])>0:
        count+=1

print(count)

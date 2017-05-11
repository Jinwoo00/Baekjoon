A=int(input())
B=int(input())
C=int(input())

result=A*B*C
result=str(result)
count=0

for i in range (0, 10):
    for j in range(0, len(result)):
        if result[j]==str(i):
            count+=1
    print(count)
    count=0

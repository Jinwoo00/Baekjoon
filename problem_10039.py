a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

array=[a, b, c, d, e]
sum=0

for i in array:
    if i<40:
        i=40
        sum+=i
    else:
        sum+=i

print(int(sum/5))

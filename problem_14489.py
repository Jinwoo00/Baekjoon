balance=input()
balance=balance.split()
chicken=int(input())

s=int(balance[0])+int(balance[1])
s_chic=chicken*2

if s_chic<=s:
    print(s-s_chic)
elif s_chic>s:
    print(s)

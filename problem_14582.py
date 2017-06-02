W=input()
S=input()

W=W.split()
S=S.split()

w_total=0
s_total=0

temp=0
for x in range(0, 9):
    w_total+=int(W[x])
    s_total+=int(S[x])

    if w_total > s_total-int(S[x]):
        temp=1

if w_total<s_total and temp==1:
    print("Yes")
else:
    print("No")

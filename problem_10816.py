N=input()
N_num=input()
M=input()
M_num=input()

N_num=N_num.split()
M_num=M_num.split()

count=0
count_arr=[]

for i in M_num:
    for j in N_num:
        if i==j:
            count+=1
    count_arr.append(count)
    count=0

for i in count_arr:
    print(i,end=' ')
    

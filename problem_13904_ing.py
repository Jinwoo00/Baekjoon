N=int(input())

d_array=[]
w_array=[]

i=0
while i<N:
    d_w=input()
    d_w=d_w.split(" ")
    
    d_array.append(int(d_w[0]))
    w_array.append(int(d_w[1]))
    
    i+=1
    

print(d_array)
print(w_array)






#d_w=input()
#d_w=d_w.split(" ")
#print(d_w)

#d_array=[]
#d_array.append(d_w[0])
#print(d_array)

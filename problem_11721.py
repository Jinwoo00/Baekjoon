input_str=input()

i=0
while(i<len(input_str)/10):
    print(input_str[i*10:(i+1)*10])
    i+=1

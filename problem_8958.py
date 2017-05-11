def OX_score(OX_str):
    score=0
    add=1
    
    for i in range(0, len(OX_str)):
        if OX_str[i]=='O':
            score+=1*add
            add+=1
        elif OX_str[i]=='X':
            add=1

    print(score)



N=int(input())
i=0

while i<N:
    OX_str=input()
    OX_score(OX_str)
    i+=1
    

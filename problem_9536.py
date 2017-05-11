T=int(input())

x=0
while x<T:
    roar=input()
    roar=roar.split()
    animal_sound=[]

    for i in range(0, 101):
        animal_sound.append(input())
        if animal_sound[i]=="what does the fox say?":
            break
        animal_sound[i]=animal_sound[i].split()
        #print(animal_sound[i][2],roar.count(animal_sound[i][2]))
    
        for j in range(0, roar.count(animal_sound[i][2])):
            del roar[roar.index(animal_sound[i][2])]
    
    
    for a in roar:
        print(a,end=' ')

    x+=1

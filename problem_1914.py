def hanoi(n, a, b, c):
    if n==1:
        print("first",a,c)
    else:
        hanoi(n-1, a, c, b)
        print("second",a,c)
        hanoi(n-1,b,a,c)

n=int(input())
hanoi(n, 1, 2, 3)

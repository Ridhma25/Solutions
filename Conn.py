for i in range(int(input())):
    n = int(input())
    if(n%2==0) or (n%7==0):
        print("YES")
    elif  n>7:
        diff = n-7
        if diff%2==0:
            print("YES")
    else:
        print("NO")

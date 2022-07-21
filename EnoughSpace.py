for i in range(int(input())):
    n,x,y = map(int, input().split())
    if (x + (y*2)) <= n:
        print("YES")
    else:
        print("NO")
        # cook your dish here

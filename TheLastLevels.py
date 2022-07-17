for i in range(int(input())):
    x,y,z = map(int, input().split())
    
    if x <= 3:
        print(x*y)
    else:
        if x%3 == 0:
            time = x//3
            print(((x*y) + (time*z)) - z)
            
        else:
            time = x//3
            print((x*y) + (time*z))

for i in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))

    count, x = 0,0
    
    l.sort()
    
    for j in range(n):
        if (x+l[j])<n:
            count += 1
        else:
            break
        x = x + l[j]
            
    print(count)

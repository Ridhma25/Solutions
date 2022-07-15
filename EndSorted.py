for i in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    
    if l[0] == 1 and l[n-1] == n:
        print(0)
    else:
        index_1 = l.index(1)
        index_n = l.index(n)
    
        final = index_1 + (n-1 - index_n)
        
        if index_1 > index_n:
            print(final-1)
        else:
            print(final)
        

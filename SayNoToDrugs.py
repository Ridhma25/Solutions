for i in range(int(input())):
    n,k,t = map(int, input().split())
    l = list(map(int, input().split()))
    
    flag = 0
    
    if l[n-1] == max(l) and l.count(l[n-1])==1:
        flag = 1 
    else:
        if k<0:
            flag = 0
        else:
            for i in range(t-1):
                l[n-1] = l[n-1] + k 
                if l[n-1] == max(l) and l.count(l[n-1])==1:
                    flag = 1 
                    break
    
    if flag == 1:
        print("Yes")
    else:
        print("No")

for i in range(int(input())):
    n = int(input())
    initial = input()
    last = input()

    count = 0
    
    for j in range(len(initial)):
        if initial[j] != last[j]:
            count +=1
            
    if count%2==0:
        print(1)
    else:
        print(0)

for i in range(int(input())):
    n = int(input())
    count = 0 
    for i in range(100):
        if n%3 != 0:
            count += 1
            n = n +1 
        else:
            break
    print(count)

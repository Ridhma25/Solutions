for i in range(int(input())):
    s,x,y,z = map(int, input().split())
    sum = x+y+z
    count = 0
    for j in range(3):
        if sum > s:
            sum = sum - max(x,y)
            count += 1
    print(count)

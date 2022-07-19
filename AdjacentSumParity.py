for i in range(int(input())):
    n = int(input())
    array = list(map(int, input().split()))
    count = 0
    for j in range(n):
        if array[j] == 1:
            count += 1
    if count%2 == 0:
        print("YES")
    else:
        print("NO")

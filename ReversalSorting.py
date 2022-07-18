for i in range(int(input())):
    flag = 1
    n, x = map(int, input().split())
    num = list(map(int, input().split()))
    for j in range(n-1):
        if(num[j] > num[j+1]):
            if (num[j] + num[j+1]>x):
                flag = 0
            else:
                temp = num[j]
                num[j] = num[j+1]
                num[j+1] = temp
    if flag == 0:
        print("NO")
    else:
        print("YES")

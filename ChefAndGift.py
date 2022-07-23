for i in range(int(input())):
    n, k = map(int, input().split())
    num = list(map(int, input().split()))
    count = 0
    for j in range(n):
        if num[j]%2 == 0:
            count += 1
    if count<k or (k==0 and count == n):
        print("NO")
    else:
        print("YES")

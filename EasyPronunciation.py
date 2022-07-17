for i in range(int(input())):
    n = int(input())
    s = input()
    l = ["a", "e", "i", "o", "u"]
    count, flag = 0, 1
    for j in range(n):
        if s[j] not in l:
            count = count +1
            if count >= 4:
                flag = 0
                break
        else:
            count = 0
    if flag == 0:
        print("NO")
    else:
        print("YES")

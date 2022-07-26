t = int(input())
for i in range(t):
    a = int(input())
    message = list(map(int, input().split()))
    count = 0
    for j in range(a):
        if(j == 0):
            if(message[j] != message[j+1]):
                count = count + 1
        elif(j == a-1):
            if(message[j] != message[j-1]):
                count = count + 1
        else:
            if(message[j-1] != message[j] or message[j] != message[j+1]):
                count = count + 1
    print(count)

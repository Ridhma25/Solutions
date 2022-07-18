for i in range(int(input())):
    n = int(input())
    counting = 0
    number = []
    array = list(map(int, input().split()))
    for j in range(n):
        number.append(array.count(array[j]))
    print(n - max(number))

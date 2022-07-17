for i in range(int(input())):
    a, b = map(int, input().split())
    score = max(a, b)
    print(7-score)

for i in range(int(input())):
    n = int(input())
    color = list(map(int, input().split()))
    colors = set(color)
    print(len(color) - len(colors))

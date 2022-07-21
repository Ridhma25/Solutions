for i in range(int(input())):
    x,y,z = map(int, input().split())
    total, price = 0,0
    for j in range(x):
        if x>total:
            total = total + y
            price += z
        else:
            break
    print(price)

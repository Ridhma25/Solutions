import math

for i in range(int(input())):
    a,b = map(int, input().split())
    if (a<b):
        while(a<b):
            a = a*2
    else:
        while(a>b):
            b = b*2
    
    if (a==b):
        print("YES")
    else:
        print("NO")

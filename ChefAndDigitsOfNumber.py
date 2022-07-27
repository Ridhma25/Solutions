for i in range(int(input())):
    s = input()
    
    count_0, count_1 = 0,0
    
    for j in s:
        if j == "0":
            count_0 += 1
        if j == "1":
            count_1 += 1
            
    if count_0 == 1 or count_1 == 1:
        print("Yes")
    else:
        print("No")

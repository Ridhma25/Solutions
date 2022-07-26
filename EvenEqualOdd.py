for i in range(int(input())):
    n = int(input())
    array = list(map(int, input().split()))
    count_even = 0
    count_odd = 0
    for j in range(2*n):
        if array[j]%2 == 0:
            count_even += 1            
    count_odd = (2*n) - count_even
    if count_even == count_odd:
        print("0")
    elif count_odd > count_even:
        print(count_odd-n)
    else:
        even = []
        for j in range(2*n):
            count = 0
            if array[j]%2==0:
                div = array[j]
                while(div%2 == 0):
                    div = div/2
                    count += 1
                even.append(count)
        even.sort()
        print(sum(even[:count_even-n]))

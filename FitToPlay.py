for i in range(int(input())):
    n = int(input())
    score = list(map(int, input().split()))
    maximum = 0
    minimum = score[0]
    for j in range(len(score)):
            maximum = max(maximum, score[j] - minimum)
            minimum = min(minimum, score[j])
    if(maximum == 0):
        print("UNFIT")
    else:
        print(maximum)

for i in range(int(input())):
    n = int(input())
    strand = list(input())
    for j in range(n):
        if strand[j] == "A":
            strand[j] = "T"
        elif strand[j] == "T":
            strand[j] = "A"
        elif strand[j] == "G":
            strand[j] = "C"
        else:
            strand[j] = "G"
    str1 = ""
    for char in strand:
        str1 += char
    print(str1)

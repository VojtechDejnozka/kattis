#https://open.kattis.com/problems/heimavinna

list = input().split(";")
total = 0
for i in range(len(list)):
    if "-" in list[i]:
        borders = list[i].split("-")
        for j in range(int(borders[0]), int(borders[1])+1):
            total += 1
    else:
        total += 1
print(total)
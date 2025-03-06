#https://open.kattis.com/problems/laegdyfirlandinu

lines = []
while True:
    try:
        line = input()
        if not line:
            break
        lines.append(line)
    except EOFError:
        break

dim = lines[0].split(" ")
lines.pop(0)

for i in range(int(dim[0])):
    lines[i] = lines[i].split(" ")

met = "Neibb"

for i in range(int(dim[0])-2):
    for j in range(int(dim[1])-2):
        actual = int(lines[i+1][j+1])
        if actual < int(lines[i+1][j]) and actual < int(lines[i][j+1]) and actual < int(lines[i+1][j+2]) and actual < int(lines[i+2][j+1]):
            met = "Jebb"
            break
    if met == "Jebb":
        break

print(met)
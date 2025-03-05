#https://open.kattis.com/problems/lettasta

lines = []
while True:
    try:
        line = input()
        if not line:
            break
        lines.append(line)
    except EOFError:
        break

problems = int(lines[0])
teams = int(lines[1])
names = lines[2].split(" ")
totals = [0] * problems

for i in range(teams):
    lines[i+3] = lines[i+3].split(" ")
    for j in range(problems):
        totals[j] += int(lines[i+3][j])
print(names[totals.index(max(totals))])
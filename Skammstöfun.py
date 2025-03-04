#https://open.kattis.com/problems/skammstofun

lines = []
while True:
    try:
        line = input()
        if not line:
            break
        lines.append(line)
    except EOFError:
        break

dim = int(lines[0])
lines.pop(0)
abbr = ""
lines = lines[0].split(" ")

for i in range(dim):
    if lines[i][0].isupper():
        abbr += lines[i][0]

print(abbr)
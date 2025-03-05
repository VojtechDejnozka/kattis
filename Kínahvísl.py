#https://open.kattis.com/problems/kinahvisl

lines = []
while True:
    try:
        line = input()
        if not line:
            break
        lines.append(line)
    except EOFError:
        break

kids = 1
for i in range(len(lines[0])):
    if lines[0][i] != lines[1][i]:
        kids += 1

print(kids)
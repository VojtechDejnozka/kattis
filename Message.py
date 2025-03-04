#https://open.kattis.com/problems/meddelande

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
message=""

down = 0

while down < int(dim[0]):
    right = 0
    while right < int(dim[1]):
        if lines[down][right] != ".":
            message += lines[down][right]
        right += 1
    down += 1

print(message)
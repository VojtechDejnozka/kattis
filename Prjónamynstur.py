#https://open.kattis.com/problems/prjonamynstur

lines = []
while True:
    try:
        line = input()
        if not line:
            break
        lines.append(line)
    except EOFError:
        break
    

chars = {".": 20, "O": 10, "\\": 25, "/": 25, "A": 35, "^": 5, "v": 22}
total = 0
dim = lines[0].split(" ")
for line in range(int(dim[0])):
    for char in range(int(dim[1])):
        total += chars[lines[line+1][char]]
print(total)
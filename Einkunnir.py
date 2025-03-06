#https://open.kattis.com/problems/einkunnir

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

answers = lines[0].split(" ")
lines.pop(0)

scores = {}
i=0
while i < (int(dim[1])*2):
    lines[i+1] = lines[i+1].split(" ")
    correct = 0
    for j in range(int(dim[0])):
        if lines[i+1][j] == answers[j]:
            correct += 1
    scores[lines[i]] = correct/int(dim[0])
    scores[lines[i]] = scores[lines[i]] + 0.00001
    scores[lines[i]] = round(scores[lines[i]],2)*10
    if scores[lines[i]].is_integer() == False:
        scores[lines[i]] = round(scores[lines[i]]*2.0) / 2.0
    i = i+2

output = ""
for i in range(len(scores)):
    if i == len(scores)-1:
        output += (list(scores)[i] + ": " + str(list(scores.values())[i]))
    else:
        output += (list(scores)[i] + ": " + str(list(scores.values())[i])) + "\n"

print(output)
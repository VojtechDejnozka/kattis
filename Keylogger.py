#https://open.kattis.com/problems/keylogger

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
alphabet = {"clank": "a", "bong": "b", "click": "c", "tap": "d", "poing": "e", "clonk": "f", "clack": "g", "ping": "h", "tip": "i", "cloing": "j", "tic": "k", "cling": "l", "bing": "m", "pong": "n", "clang": "o", "pang": "p", "clong": "q", "tac": "r", "boing": "s", "boink": "t", "cloink": "u", "rattle": "v", "clock": "w", "toc": "x", "clink": "y", "tuc": "z"}
special = {"whack": "spacebar", "bump": "capslock", "pop": "delete", "dink": "shiftdown", "thumb": "shiftup"}
message = ""
caps = False
shift = False

for i in range(dim):
    if lines[i] in alphabet.keys():
        if (caps == True or shift == True) and not (caps == True and shift == True):
            message += alphabet[lines[i]].capitalize()
        else:
            message += alphabet[lines[i]]
    elif lines[i] in special.keys():
        if special[lines[i]] == "spacebar":
            message += " "
        elif special[lines[i]] == "capslock":
            if caps == False:
                caps = True
            else:
                caps = False
        elif special[lines[i]] == "delete":
            message = message[:-1]
        elif special[lines[i]] == "shiftdown":
            shift = True
        elif special[lines[i]] == "shiftup":
            shift = False

print(message)
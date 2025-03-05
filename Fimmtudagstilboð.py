#https://open.kattis.com/problems/fimmtudagstilbod

input = int(input())
base = 1000
add = 100
if input >= 1993 and input <= 2020:
    print(base)
else:
    print(base + ((input-2020)*add))
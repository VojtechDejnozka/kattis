#https://open.kattis.com/problems/fjoldibokstafa
import re

input = str(input())
input = re.findall("[a-zA-Z]", input)
print(len(input))
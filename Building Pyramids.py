#https://open.kattis.com/problems/pyramids

input = int(input())
layers = 0
constraint = 1

while input >= constraint:
    layers += 1
    input = input - constraint
    constraint = ((int(constraint**(1/2))) + 2)**2

print(layers)
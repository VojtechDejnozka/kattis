#https://open.kattis.com/problems/hlaupafmaeli

input = int(input())
age = 0
diff = 0

age = input - 2000
if age>=100:
    diff = age//100

addit = diff//4
age = (((age-20)//4)-diff)+addit

if (input%4 == 0 and input%100 !=0) or input%400 == 0:
    print(int(age))
else:
    print("Neibb")



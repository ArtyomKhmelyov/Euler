__author__ = 'artyom'
Result = 0
for i in range(1000):
    if i % 15 == 0:
        Result += i
    elif i % 3 == 0:
        Result += i
    elif i % 5 == 0:
        Result += i
print(Result)
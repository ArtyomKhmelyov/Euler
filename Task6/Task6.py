Result = 0
for i in range(1, 101):
    for j in range(i, 101):
        if i != j:
            Result += 2*i*j
print Result

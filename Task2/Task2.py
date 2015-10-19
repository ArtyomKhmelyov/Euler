def fib(n):
    if n == 0:
        return 0
    elif n == -1 or n == 1:
        return 1
    else:
        if n > 0:
            return fib(n-1) + fib(n-2)
        else:
            return fib(n+2) - fib(n+1)


Result = 0
for i in range(60):
    if fib(i) > 4000000:
        break
    if fib(i) % 2 == 0:
        Result += fib(i)
print Result


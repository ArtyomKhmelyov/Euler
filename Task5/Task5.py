const = 2520

def Result(n):
    for i in range(2, 20):
        if n % i != 0:
            return False
    return True

while const < 222222222222:
    if Result(const):
        print const
        break
    else:
        const += 1

print

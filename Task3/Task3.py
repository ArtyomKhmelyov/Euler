import math
const = 600851475143
Result = 0

def IsPrime(n):
    if n % 2 == 0:
        return False
    else:
        for i in range(3, int(math.sqrt(n))):
            if n % i == 0:
                return False
    return True

i = 1
while i < math.sqrt(const):
    if IsPrime(i) and const % i == 0:
        Result = i
    i += 1

print Result


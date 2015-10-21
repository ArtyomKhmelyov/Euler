def IsPrime(n):
    if n % 2 == 0:
        return False
    else:
        for i in range(3, int(n/2)):
            if n % i == 0:
                return False
    return True


a = 1
b = 2
while b <= 1000000:
    if a == 6:
        break
    if IsPrime(b):
        a += 1
    b += 1

print b-1, a



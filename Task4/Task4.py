def isPalindrome(n):
    if str(n)[::-1] == str(n):
        return True
    else:
        return False

Result = 0
for i in range(100, 999):
    for j in range(100, 999):
        if isPalindrome(i*j):
            if i*j > Result:
                Result = i*j

print Result

def isPif(a,b,c):
	if a**2 + b**2 == c**2:
		return True
	else:
		return False

buf = True
m = 11
while buf:
	for n in range(1,m):
		a = 2*m*n
		b = m**2 - n**2
		c = m**2 + n**2
		if isPif(a,b,c) and a + b + c == 1000:
			buf = False
			print a,b,c, a*b*c 
	m += 1






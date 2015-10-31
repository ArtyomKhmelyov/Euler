import math
result = 2
array = []
for i in range(3,2000000,2):
	buf = True
	for j in range(2,int(math.sqrt(i))+1):
		if i % j == 0:
			buf = False
			break
	if buf:
		result += i
print result

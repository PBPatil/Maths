n = int(raw_input('Enter n : '))

a,b = 0,1

print a
print b

'''left = n - 2

while left > 0:
	c = a + b
	print c
	left = left - 1

	a = b
	b = c'''
for no in range(1,n-1):
		c = a + b
		print c

		a = b 
		b = c

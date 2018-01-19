def fibo(n):
	a, b = 0, 1
	print a
	print b
	'''left = n - 2
		while left > 0:
		c = a + b
		print c
		left = left - 1

		a = b
		b = c'''

	for no in range(1, n - 1):
		c = a + b
		print c

		a = b 
		b = c




def neven(n):
	for no in range(0, n + 1, 2):
		print no


def evenodd(n):
	if n % 2 == 0:
		print str(n) + ' is even'
	else:
		print str(n) + ' is odd'

while True:
	print '1- Fibo Series\n2-even series\n3-even or odd\n4-exit'
	ch  = int(raw_input('enter choice :'))
	
	if not ch == 4:
		n = int(raw_input('enter n :'))

	if ch == 1:
		fibo(n)
	elif ch == 2:
		neven(n)
	elif ch == 3:
		evenodd(n)
	else:
		break




num = int(raw_input('Enter no: '))
def ran_check(num,low,high):
	if num in range(4,11):
		print ' %s is in the range' %str(num)
	else:
		print'This is out of the range.'
print ran_check(num,4,11)	 

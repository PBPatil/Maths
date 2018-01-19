n = int(raw_input('Enter n :  '))

'''i = 0 

while i <= n :
    if i % 2 == 0:
          print i
    i = i + 1'''
nos = range(0,n+1)
'''for no in range(0,n+1):
    if no % 2 == 0:
       print no'''

for no in range(0,n+1,2):
    if no > 10:
        break
    print no 
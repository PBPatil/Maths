length = 10 #global
bredth = 5  #global

def area():
    #in python global varibales can be accessed
    # even in the functions defined in the same file
    # only refer their values
    return length*bredth

def perimeter(length,bredth):
    # length and bredth are local here to the
    # perimeter function
    return 2 * (length + bredth)

print area()
print perimeter(5,3)

x = 7 #Global
y = 9
z = 5
def func():
    x = 9 #local
    print x #9
    # this is error
    ''' y = y + 10
        print y'''
    
     global z #dont do it!
     #z will be treated as global in func
     z = z * 3
     print z #15
    
func()
print x #7
print y
print z #15

n = 10
if n % 2 == 0:
   msg = 'Is even'
else:
   msg = 'Is odd

print msg

''' In Python only functions create scope.
Rest of the block (if,elif,loops,class)
do not create a scope'''

'''scope of a variable is always
nearest enclosing scope'''
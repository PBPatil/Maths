length = float(raw_input('Enter length : '))
bredth = float(raw_input('Enter bredth : '))

def perimeter(l=3,b=2):
    # Default values to parameters of function
    # default parameter cannot have non default
    # parameters declared after it
    p = 2 * (l+b)
    return p

per = perimeter(length, bredth)
print per

print perimeter(6)
print perimeter(b=2.5)

#Keyword arguments
print perimeter(b=8,l=10)

# -------------------------------------- Task 1 -----------------------------------
def add(x, y):
    return x + y
def sub(x, y):
    return x - y
def div(x, y):
    return x / y
def mult(x, y):
    return x * y
def exp(x, y):
    return x ** y

# TODO: Add definitions of sub(), div(), mult(), exp(), as well as neg() and sqrt().
#       neg() should return the negation of the given number, and sqrt() should
#       return the square root of the given number. 

def neg(x):
    return -x

     # fill here

def sqrt(x):
    return x ** (1/2)
     # fill here

# -------------------------------------- Task 2 -----------------------------------

# TODO: Implement the quadratic formula using *only* the functions defined here.
#       Do not use arithmetic operators directly. 
#       You're allowed to define other functions.
a = 1
b = -3
c = 1

#(-b +- (b ** 2 - 4 * a * c) **1/2)/2*a 
#x1 = ((neg) + ((exp) - (mult * c))(sqrt)/2*a) # TODO: write a code to compute the first root of the quadratic equation
#x2 = ... # TODO: then do the same for the second root
# Note: Make sure to remove the ellipsis (...) when you're writing your code
# x1 = (neg (b)+(((b) exp (2)) sub((4) mult (a) mult (c))))
# x1 =     div add (neg(b),(sqrt(sub(exp(b,2), (mult(mult(4,a),c)), )))), mult(2, a)
x1 =div (add(neg(b), sqrt(sub(exp(b , 2), mult(mult (4 , a), c)))), mult(2, a))
x2 =div (sub(neg(b), sqrt(sub(exp(b , 2), mult(mult (4 , a), c)))), mult(2, a))
print("First root:" + str(x1))
print("Second root:" + str(x2))

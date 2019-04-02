# this is used for testing unknown-funcs
from sympy import *
import scipy.integrate
def f(alpha,x):
	if x<5:
		return x
	else:
		return alpha-x

#x = symbols('x')
#y = integrate(f(x),(x,0,8))
y = scipy.integrate.quad(f(alpha=10), 1, 9)
print(y)

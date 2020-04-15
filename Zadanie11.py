from math import *
import scipy.integrate as integrate

def f(x):
  return sin(pi*(1+sqrt(x))/(1+pow(x,2)))*pow(e,-1*x)

a = 7*log1p(10)

result = integrate.romberg(f,0,a)
print("Result is: ")
print(result)
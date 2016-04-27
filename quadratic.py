#!/usr/bin/python
import sys
import math

#Python script that returns the roots of a quadratic equation
#of the form a*x^2 + b*x + c = 0
#Enter values for a, b, and c in the command line
#e.g. run: >python quadratic.py 1 2 -15
def main():
    a = sys.argv[1]
    b = sys.argv[2]
    c = sys.argv[3]

    assert a.isdigit() and b.isdigit() and c.isdigit(), "One of your inputs in not numeric! \n  Please try again."
    assert float(a) != 0, "You entered a leading coefficient of 0. Please try again."

    x1, x2 = find_roots(a, b, c)
    print ("This is x1: %f" %x1)
    print ("This is x2: %f" %x2)


def find_roots(a,b,c):
    
    a = float(a)
    b = float(b)
    c = float(c)
    mid = (b**2) - 4*a*c
    sqrt_mid = 0
    try: 
	 sqrt_mid = math.sqrt(mid)
    except ValueError as e:
    	print(e.args)
	exit()
	
    x1 = (-b + sqrt_mid)/(2*a)
    x2 = (-b - sqrt_mid)/(2*a)
    return x1, x2


if __name__=="__main__":
        main()

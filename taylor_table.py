"""
Program to compute coefficients for finite difference approximations
of arbitrary derivatives
"""
from math import factorial
import numpy as np


def taylor_table(order, m_down, m_up):
    """
    compute coefficients for difference approximation, given input:
    order: The order of derivative to be approximated
    m_down: no. of points to the left (negative index shifts)
    n_up: no. of points to the right (positive index shifts)
    """
    N = m_down +m_up +1 # number of points

    if order >= N:
        print("Not enough points for requested order")
        return

    b = np.zeros(N)
    b[order] = factorial(order)
    A = np.array([np.arange(-m_down,m_up+1)**i for i in range(N)])
    
    coeff = np.linalg.solve(A,b)
    print(coeff)



if __name__ == "__main__":
    # example usage
    
    taylor_table(2,2,2)

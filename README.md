# NLAB1 Assignment 1


## Problem 1

A program using a Taylor table to generate finite difference approximations can be found in this repository. The program can compute the coefficients for finite difference approximations of arbitrary order derivatives, provided a suitable stencil is given.
Test the program by finding non-zero coefficients (a,b,c,d,e) approximating the second derivative of a smooth enough function $u$ for the following two cases:

1. Symmetric Case:

$$ \frac{au(x-2h)+b u(x-h)+c u(x) + d u(x+h)+ e u(x+2h)}{h^2}	= u''(x) + \mathcal O(h^{r_1})$$

2. Nonsymmetric Case:

$$ \frac{a u(x-h) +b u(x)+c  u(x+h)+ d u(x+2h)+ e u(x+3h)}{h^2}	=  u''(x)+ \mathcal O(h^{r_2}) $$


Report the coefficients and the expected order of convergence for both cases. Test the approximation for the function

$$ u(x) = \sin (2\pi x) $$


To that end, evaluate the difference approximation and the exact second derivative on a grid 
```math
	\mathcal G_h:= \{ i h : i=0,\dots N-1  ; h N = 1 \} $$
```
and enforce periodic boundary conditions $u_i = u_{i+N}$ as needed.  

Plot the error in maximum norm (i.e., the maximum absolute value of the error, taken over all grid points) against grid size for $N=10,100,1000$. Make sure to check whether you achieve the expected order of convergence. 


## Problem 2

Consider the approximation
```math
	\frac{u(x-h) -2 u(x) + u(x+h)}{h^2}	= u''(x)+ \mathcal O(h^2). 
```
Measure the error as in Problem 1 using the function 

```math
	u(x) = (\sin (\pi x))^\alpha \notag
```
for  $\alpha=3.5$ and $\alpha=4.5$. Does the approximation of the second derivative converge at second order  for both values of $\alpha$? Explain your observations!

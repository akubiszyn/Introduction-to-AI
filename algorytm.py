import autograd.numpy as np
from autograd import grad

list_of_xk = []

def fun(x):
    return x**2 + 5

def get_xk(function, x0, a):
    gradient= grad(function)
    xk = x0 - a * gradient(x0)
    return xk

def compute_proper_xk(function, x0, a):
    xk = get_xk(function, x0, a)
    k = 5
    while function(xk) >= function(x0):
        k -= 1
        a -= 0.2
        xk = get_xk(function, x0, a)
        if k == 0:
            return
    return xk

def gradient_algorithm(function, x0, a, k):
    xk = compute_proper_xk(function, x0, a)
    if abs(xk - x0) < 10**(-3):
        return xk
    list_of_xk.append(xk)
    xk = gradient_algorithm(function, xk, a, k=5)
    return xk


print(gradient_algorithm(fun, np.array([20]), 0.7, 5))

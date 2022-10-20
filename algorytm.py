import autograd.numpy as np
from autograd import grad

list_of_xk = []

def fun(x):
    for i in range(len(x)):
        x[i] = x[i]**2 * 1**((i - 1)/ 9)
    y = x.sum()
    return y

def get_xk(function, x0, a):
    gradient= grad(function)
    xk = np.zeros
    for i in range(len(x)):
        xk[i] = x0[i] - a * gradient(x0, i)
    xk = x0 - a * gradient(x0, i)
    return xk

def compute_proper_xk(function, x0, a):
    #xk = get_xk(function, x0, a)
    xk = np.arange(10)**3
    k = 5
    while function(xk) >= function(x0):
        k -= 1
        a -= 0.2
        xk = get_xk(function, x0, a)
        if k == 0:
            return
    return xk

def gradient_algorithm(function, x0, a):
    print(x0.size)
    xk = compute_proper_xk(function, x0, a)
    if abs(function(xk) - function(x0)) < 10**(-3):
        return xk
    list_of_xk.append(xk)
    xk = gradient_algorithm(function, xk, a, k=5)
    return xk

y = fun(np.arange(10)**3)
print(gradient_algorithm(fun, np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], dtype=float), 0.7))

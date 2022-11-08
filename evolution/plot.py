from evolutionary_algo import evolutionary_algorithm
import numpy as np

def get_function(n, alpha):
    def function(x):
        a = np.zeros(n)
        for i in range(n):
            a[i] = alpha ** ((i - 1) / (n - 1))
        y =  np.sum((x**2) * a)
        return y

    return function

fun = get_function(10,1)
x_min, o_min = evolutionary_algorithm(10, fun, 30, 20, 0.5, (-100, 100))
print(x_min, o_min)

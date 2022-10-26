import autograd.numpy as np   # Thinly-wrapped version of Numpy
from autograd import grad

# def fun(x):
#     a = np.zeros((2))
#     for i in range(2):
#         a[i] = 1**((i - 1)/ 9)
#     y =  np.sum((x**2) * a)
#     return y



# x0 = np.array([1, 2], dtype=float)

# y = fun(x0)

# for i in range(len(x0)):
#     gradient_i= grad(fun, 0)
#     b = gradient_i(x0)

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = a * b
print(c)


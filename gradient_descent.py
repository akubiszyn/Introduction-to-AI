import autograd.numpy as np
from autograd import grad


def get_x1(fun, x0, length_step):
    gradient = grad(fun)
    x1 = x0 - length_step * gradient(x0)
    return x1

def compute_proper_x1(fun, x0, length_step, reduction, limit, steps):
    x1 = get_x1(fun, x0, length_step)
    while fun(x1) >= fun(x0):
        limit -= 1
        if limit == 0:
            return None
        length_step *= reduction
        x1 = get_x1(fun, x0, length_step)
    return x1

def gradient_algorithm(fun, x0, length_step, reduction, limit):
    steps = [fun(x0)]
    x1 = compute_proper_x1(fun, x0, length_step, reduction, limit, steps)
    while(x1 is not None):
        steps.append(fun(x1))
        if abs(fun(x1) - fun(x0)) < 10**(-3):
            break
        x0 = x1
        x1 = compute_proper_x1(fun, x0, length_step, reduction, limit, steps)

    return steps

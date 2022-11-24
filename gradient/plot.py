import autograd.numpy as np
from matplotlib import pyplot as plt
from gradient_descent import gradient_algorithm
import time
import gc
import sys
sys.path.insert(0, '/home/alicja/Studia/3sem/WSI/wsi/cec2017-py/cec2017')
from functions import f1, f9


def get_function(n, alpha):
    def function(x):
        a = np.zeros(n)
        for i in range(n):
            a[i] = alpha ** ((i - 1) / (n - 1))
        y =  np.sum((x**2) * a)
        return y

    return function
# 'alpha =' + str(10**alpha) + ',

def generate_plot(steps, time, alpha):
    keys1 = [ i for i in range(len(steps))]
    values1 = [i for i in steps]
    label_legend =  'time: ' + str(round(time, 5))
    label_legend += ', iterations: ' + str(len(steps)) + ', value:' + str(round(steps[-1], 5))
    plt.plot(keys1, values1, '-o', label=label_legend)
    plt.legend()
    plt.yscale('symlog')
    plt.title("Gradient descent depending on parameter alpha")

def get_data(alpha):
    gc_old = gc.isenabled()
    gc.disable()
    fun = get_function(10, 10**alpha)
    start = time.process_time()
    steps = gradient_algorithm(
        f1,
        np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], dtype=float),
        0.1,
        0.1,
        300)
    stop = time.process_time()
    if gc_old: gc.enable()
    algorithm_time = stop - start
    return steps, algorithm_time

for i in range(1):
    data = get_data(i)
    generate_plot(data[0], data[1], 0)
plt.show()
import autograd.numpy as np
from matplotlib import pyplot as plt
from qlearning_algorithm import qlearning
import gc
import time

def generate_plot(gamma, beta, epsilon):
    data = get_data(gamma, beta, epsilon)
    steps = data[0]
    time = data[1]
    keys1 = [ i for i in range(len(steps))]
    values1 = [i for i in steps]
    # label_legend =  'time: ' + str(round(time, 5))
    label_legend = 'gamma = ' + str(gamma) + ', beta = ' + str(beta) + ', epsilon = ' + str(epsilon) + ', time = ' + str(time)
    plt.plot(keys1, values1, '-o', label=label_legend)
    plt.legend()
    plt.xscale('symlog')
    plt.title("Q-learning algorithm")

def get_data(gamma, beta, epsilon):
    gc_old = gc.isenabled()
    gc.disable()
    start = time.process_time()
    steps = qlearning(10000, 100, gamma, beta, epsilon, 500, 6)[1]
    stop = time.process_time()
    if gc_old: gc.enable()
    algorithm_time = stop - start
    return steps, algorithm_time

generate_plot(0.99, 0.5, 1)
# generate_plot(0.99, 0.5, 0.1)
plt.show()
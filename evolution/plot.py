from evolutionary_algo import evolutionary_algorithm
import numpy as np
from matplotlib import pyplot as plt
import sys
import time
import gc
sys.path.insert(0, '/home/alicja/Studia/3sem/WSI/wsi/cec2017-py/cec2017')
from functions import f1, f9


def generate_plot(values, time):
    print(values[-1])
    keys1 = [ i for i in range(len(values))]
    values1 = [i[1] for i in values]
    label_legend = 'time: ' + str(round(time, 5)) + ", min value: " + str(round(values[-1][1]))
    plt.plot(keys1, values1, '-o', label=label_legend)
    plt.legend()
    plt.yscale('symlog')
    plt.title("Evolutionary algorithm, iteraitions: 1000, population: 20, sigma: 5")    


def get_data():
    gc_old = gc.isenabled()
    gc.disable()
    start = time.process_time()
    values = evolutionary_algorithm(10, f9, 1000, 20, 5, (-100, 100))
    stop = time.process_time()
    if gc_old: gc.enable()
    algorithm_time = stop - start
    return values, algorithm_time
data = get_data()
generate_plot(data[0], data[1])
plt.show()

import sys
from matplotlib import pyplot as plt
from algorytm import fun, list_of_xk


def generate_plot():
    keys1 = [ i for i in range(-10, 11)]
    values1 = [i**2 + 5 for i in range(-10, 11)]
    keys2 = [i for i in range(len(list_of_xk))]
    values2 = [fun(xk) for xk in list_of_xk]
    plt.plot(keys1, values1, '-')
    plt.plot(keys2, values2, 'o')
    #plt.legend()
    #plt.title()
    #plt.xticks(rotation=30, fontsize='xx-small', horizontalalignment='right')
    #buffer = BytesIO()
    #plt.savefig(buffer)
    plt.show()

generate_plot()
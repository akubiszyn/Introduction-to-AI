import random
import numpy as np

def rating(fun, population, population_number):
    o = np.zeros(population_number)
    for i in range(population_number):
        o[i] = fun(population[i])
    return o

def find_best(population, o):
    o_min = np.min(o)
    index = np.where(o == o_min)[0][0]
    x_min = population[index]
    return x_min, o_min

def initiation(population_number, dimension, domain):
    population = np.random.uniform(domain[0], domain[1], (population_number, dimension))
    return population

def reproduction(Pt, o, population_number, dimension):
    R = np.zeros((population_number, dimension))
    for i in range(population_number):
        tournament = random.choices(range(population_number), k=2)
        if o[tournament[0]] <= o[tournament[1]]:
            R[i] = Pt[tournament[0]]
        else:
            R[i] = Pt[tournament[1]]
    return R

def gen_operation(population, sigma, population_number):
    for i in range(population_number):
        population[i] = population[i] + sigma * np.random.normal(0, 1, 10)
    return population

def elit_succesion(Pt, M, k, o):
    for i in range(k):
        x = find_best(Pt,o)[0]
        M = np.vstack((M, x))
        index = np.where(Pt == x)[0][0]
        Pt = np.delete(Pt, index, axis=0)
        o = np.delete(o, index, axis=0)
    return M

def evolutionary_algorithm(dimension, fun, tmax, population_number, sigma, domain):
    values = []
    t = 0
    P0 = initiation(population_number, dimension, domain)
    o = rating(fun, P0, population_number)
    x_min, o_min = find_best(P0, o)
    Pt = P0
    while(t < tmax):
        R = reproduction(Pt, o, population_number, dimension)
        M = gen_operation(R ,sigma, population_number)
        o = rating(fun, M, population_number)
        xt, ot = find_best(M, o)
        if ot <= o_min:
            o_min = ot
            x_min = xt
        Pt = elit_succesion(Pt, M, 1, o)
        t += 1
        values.append((x_min, o_min))
    return values
    

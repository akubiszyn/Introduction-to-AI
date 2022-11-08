import random
import numpy as np

def rating(fun, population, population_number):
    o = np.zeros(population_number)
    for i in range(population_number):
        o[i] = fun(population[i])
    return o

def find_best(population, fun, population_number):
    o = rating(fun, population, population_number)
    o_min = min(o)
    index = np.where(o == o_min)[0][0]
    x_min = population[index]
    return x_min, o_min

def initiation(population_number, dimension, domain):
    population = np.random.uniform(domain[0], domain[1], (population_number, dimension))
    return population

def reproduction(Pt, o, population_number):
    R = np.zeros(population_number)
    for i in range(population_number):
        tournament = random.choices(Pt, 2)
        R[i] = min(tournament[0], tournament[1])
    return R

def gen_operation(population, sigma, population_number):
    for i in range(population_number):
        population[i] = population[i] + sigma * np.random.normal(0, 1)
    return population

def elit_succesion(Pt, M, k, fun, population_number):
    for i in range(k):
        x, o = find_best(Pt, fun, population_number)
        M = np.append(x)
        index = np.where(Pt == x)[0][0]
        Pt = np.delete(Pt, index, axis=0)
        o = np.delete(o, index, axis=0)
    return M

def evolutionary_algorithm(dimension, fun, tmax, population_number, sigma, domain):
    t = 0
    P0 = initiation(population_number, dimension, domain)
    x_min, o_min = find_best(P0, fun, population_number)
    Pt = P0
    while(t < tmax):
        R = reproduction(Pt, o, population_number)
        M = gen_operation(R ,sigma, population_number)
        xt, ot = find_best(M, fun, population_number)
        if ot <= o_min:
            o_min = ot
            x_min = xt
        Pt, o = elit_succesion(Pt, M, 1, fun, population_number)
        t += 1
    

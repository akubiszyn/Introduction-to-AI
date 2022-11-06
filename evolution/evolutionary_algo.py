import random
import numpy as np


def find_best(P0, o):
    return

def initiation(population_number, dimension):
    population = np.random.randn((population_number, dimension), dtype=float)
    return 

def rating(fun, population):
    return

def gen_operation(population, sigma, population_number):
    for i in range(population_number):
        population[i] = population[i] + sigma * np.random.normal(0, 1)
    return population

def reproduction(Pt, o, population_number):
    R = np.zeros(population_number)
    for i in range(population_number):
        tournament = random.choices(Pt, 2)
        R[i] = min(tournament[0], tournament[1])
    return R

def succesion(Pt, M, o, om):
    return

def evolutionary_algorithm(dimension, fun, tmax, population_number):
    t = 0
    P0 = initiation(population_number, dimension)
    o = rating(fun, P0)
    xs, os = find_best(P0, o)
    while(t < tmax):
        R = reproduction(Pt, o, population_number)
        M = gen_operation(R ,sigma, population_number)
        om = rating(fun, M)
        xt, ot = find_best(M, om)
        if ot <= os:
            os = ot
            xs = xt
        Pt1, o = succesion(Pt, M, o, om)
        t += 1
    

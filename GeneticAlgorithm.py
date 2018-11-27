import numpy
import math
import random
from random import randint as rdi
from matplotlib import pyplot as pl
from fuzzyNetwork import get_aptitude

def get_population(alleles, chromosomes, individuals):    
    population = numpy.random.randint(2**alleles, size=(individuals, chromosomes))

    return population


def tournament(population, individuals, number_of_contestants):
    contestants = numpy.random.randint(individuals, size=number_of_contestants)
    winner = population[min(contestants)]

    return winner


def numbers_to_string(individual):
    binary_string = ''.join(["{:08b}".format(item) for item in individual])

    return binary_string


def get_child(father, mother, population, individuals):
    cut_distance = random.randint(1,len(father)-1)

    father_x = father[:cut_distance]
    father_y = father[cut_distance:]
    mother_x = mother[:cut_distance]
    mother_y = mother[cut_distance:]

    child1 = father_x + mother_y
    child2 = mother_x + father_y

    #Mutation
    mutation_numbers = numpy.random.randint(len(father), size=math.ceil(len(father)*mutation_probability))
    
    if cut_distance in mutation_numbers:
        mutation_bit = random.randint(1,len(father)-1)

        if child1[mutation_bit-1] is '0':
            child1 = child1[:mutation_bit - 1] + '1' + child1[mutation_bit:]
        elif child1[mutation_bit-1] is '1':   
            child1 = child1[:mutation_bit - 1] + '0' + child1[mutation_bit:]
    
    return child1, child2


def string_to_numbers(alleles, chromosomes, individual):
    numbers = numpy.empty([chromosomes], dtype=int)

    for i in range(chromosomes):
        numbers[i] = int(individual[i*alleles:(i+1)*alleles], 2)

    return numbers


alleles = 8
chromosomes = 5*4 
individuals = 1500
mutation_probability = 0.05
generations = 100
number_of_contestants = int(individuals*.05)

population = get_population(alleles, chromosomes, individuals)

for gen in range(generations):
    new_population = []
    for i in range(int(individuals/2)):
        father = tournament(population, individuals, number_of_contestants)
        mother = tournament(population, individuals, number_of_contestants)
        
        father_b = numbers_to_string(father)
        mother_b = numbers_to_string(mother)
        child1_bin, child2_bin = get_child(father_b, mother_b, population, individuals)
        child_1 = string_to_numbers(alleles, chromosomes, child1_bin)
        child_2 = string_to_numbers(alleles, chromosomes, child2_bin)

        new_population.append([child_1, get_aptitude(child_1)])
        new_population.append([child_2, get_aptitude(child_2)])

    results = sorted(new_population, key=lambda x:(x[1][0]))
    
    print('gen:', gen)
    print(results[0][1])
    
    input_plot = [17.53, 16.94, 8.84, 12.13, 22.01, 12.65, 12.67,23.98,14.13,11.76,10.33,0,0,0]

    

    for individual in range(individuals):
        population[individual]=results[individual][0]

pl.plot(input_plot, "blue", results[0][1][1], "red")
pl.show()
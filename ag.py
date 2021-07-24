import random
import math


class Individual:
    def __init__(self):
        self.x1 = (random.uniform(0, 10))
        self.x2 = (random.uniform(0, 10))
        self.fitness = 0
        self.objective_function_value = 0
        self.ranking_selection_value = 0

    def setFitness(self, newFitness):
        self.fitness = newFitness


class Population:
    def __init__(self, populationSize):
        self.population = []

        for i in range(0, populationSize):
            self.population.append(Individual())


def func_alpine_2(individual):
    return ((math.sqrt(individual.x1) * math.sin(individual.x1)) * (math.sqrt(individual.x2) * math.sin(individual.x2)))


def func_fitness(objective_function_rank, size_population):
    max = size_population
    min = 1

    return min + ((max - min) * ((size_population - objective_function_rank) / (size_population - 1)))


def ranking_selection(population_ordered_by_fitness: list[Individual]):
    total_ranking = 0

    for rank in len(population_ordered_by_fitness):
        total_ranking = total_ranking + rank

    for index, individual in enumerate(population_ordered_by_fitness):
        individual.ranking_selection_value = index/total_ranking


def select_random_individual(population: list[Individual]):
    value = (random.uniform(0, 10))
    current_rank = 0

    for index, individual in enumerate(population):
        current_rank = current_rank + individual.ranking_selection_value
        if(current_rank >= value):
            return individual


def crossover(individual1: Individual, individual2: Individual):
    value = (random.uniform(0, 1))
    new_individual = Individual()

    if(value >= 0.5):
        new_individual.x1 = individual1.x1
        new_individual.x2 = individual2.x2
        return new_individual

    new_individual.x1 = individual2.x1
    new_individual.x2 = individual1.x2
    return new_individual


# helpers -----------------------------------

def order_population_by_objective_function_value(population: list[Individual]):
    return sorted(population, key=lambda individual: individual.objective_function_value, reverse=True)


pop = Population(5)

for individual in pop.population:
    print("\n New Individual:")
    print(individual.x1)
    print(individual.x2)
    individual.objective_function_value = func_alpine_2(individual)
    print(f"alpine: {individual.objective_function_value}")

ordered_list = order_population_by_objective_function_value(pop.population)

print("\n objective_function_value:")
for i, individual in enumerate(ordered_list):
    print(f"{i} : {individual.objective_function_value}")
print("\n")

for rank, individual in enumerate(ordered_list):
    print(f"fitness: {func_fitness(rank+1, len(pop.population))}")

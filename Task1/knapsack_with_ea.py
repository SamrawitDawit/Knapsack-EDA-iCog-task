import random 

def knapsack_eda(values, weights, capacity, population_size = 50, generations = 100, elite_size = 10):
    n = len(values)

    # Initializing a random population of binary solutions
    def initialize_population():
        return [[random.randint(0, 1) for _ in range(n)] for _ in range(population_size)]
    
    #Evaluating the fitness of a solution
    def fitness(solution):
        total_value = sum(v for v, selected in zip(values, solution) if selected)
        total_weight = sum(w for w, selected in zip(weights, solution) if selected)

        if total_weight > capacity:
            return 0
        return total_value
    
    #Selecting the top elite_size individuals based on fitness
    def select_elite(population):
        scored_population = [(individual, fitness(individual)) for individual in population ]
        scored_population.sort(key=lambda x: x[1], reverse=True)
        return [individual for individual, score in scored_population[:elite_size]]
    
    #Building a probabilistic model of the elite population(probability of selecting each item)
    def build_probabilistic_model(elite_population):
        probabilities = [0] * n
        for individual in elite_population:
            for i in range(n):
                probabilities[i] += individual[i]
        return [p / elite_size for p in probabilities]
    
    #Generatig a new population by sampling from the probabilistiic model
    def sample_new_population(probabilities):
        new_population = []
        for _ in range(population_size):
            individual = [1 if random.random() < probabilities[i] else 0 for i in range(n)]
            new_population.append(individual)
        return new_population
    

    population = initialize_population()
    best_solution = None
    best_value = 0

    for generation in range(generations):
        elite_population = select_elite(population)
        probabilities = build_probabilistic_model(elite_population)
        population = sample_new_population(probabilities)

        for individual in elite_population:
            value = fitness(individual)
            if value > best_value:
                best_value = value
                best_solution = individual
    return best_solution, best_value
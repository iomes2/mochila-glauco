import numpy as np
from typing import List, Tuple, Dict
 
 
class GeneticKnapsack:
    """
    Solução para o problema da Mochila 0/1 usando Algoritmo Genético
    """
 
    def __init__(self, weights: List[int], values: List[int], capacity: int,
                 pop_size: int = 100, generations: int = 100,
                 crossover_rate: float = 0.8, mutation_rate: float = 0.1):
        self.weights = np.array(weights)
        self.values = np.array(values)
        self.capacity = capacity
        self.pop_size = pop_size
        self.generations = generations
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate
        self.n_items = len(weights)
 
        if len(weights) != len(values):
            raise ValueError("As listas de pesos e valores devem ter o mesmo tamanho")
        if any(w <= 0 for w in weights) or any(v <= 0 for v in values):
            raise ValueError("Pesos e valores devem ser positivos")
        if capacity <= 0:
            raise ValueError("A capacidade da mochila deve ser positiva")
 
    def initialize_population(self) -> np.ndarray:
        return np.random.randint(0, 2, size=(self.pop_size, self.n_items))
 
    def fitness(self, solution: np.ndarray) -> Tuple[float, int, int]:
        total_weight = np.sum(solution * self.weights)
        total_value = np.sum(solution * self.values)
        if total_weight > self.capacity:
            return 0, total_value, total_weight
        return total_value, total_value, total_weight
 
    def evaluate_population(self, population: np.ndarray) -> Tuple[np.ndarray, List[Tuple[float, int, int]]]:
        fitness_values = np.zeros(self.pop_size)
        details = []
        for i in range(self.pop_size):
            fit, val, wt = self.fitness(population[i])
            fitness_values[i] = fit
            details.append((fit, val, wt))
        return fitness_values, details
 
    def selection(self, population: np.ndarray, fitness_values: np.ndarray) -> np.ndarray:
        tournament_size = 3
        new_pop = np.zeros_like(population)
        for i in range(self.pop_size):
            candidates = np.random.choice(self.pop_size, tournament_size, replace=False)
            best = candidates[np.argmax(fitness_values[candidates])]
            new_pop[i] = population[best]
        return new_pop
 
    def crossover(self, population: np.ndarray) -> np.ndarray:
        new_pop = population.copy()
        for i in range(0, self.pop_size - 1, 2):
            if np.random.random() < self.crossover_rate:
                point = np.random.randint(1, self.n_items)
                new_pop[i, point:], new_pop[i + 1, point:] = new_pop[i + 1, point:].copy(), new_pop[i, point:].copy()
        return new_pop
 
    def mutation(self, population: np.ndarray) -> np.ndarray:
        for i in range(self.pop_size):
            for j in range(self.n_items):
                if np.random.random() < self.mutation_rate:
                    population[i, j] = 1 - population[i, j]
        return population
 
    def elitism(self, old_pop: np.ndarray, new_pop: np.ndarray,
                old_fit: np.ndarray, new_fit: np.ndarray,
                elite_size: int = 2) -> Tuple[np.ndarray, np.ndarray]:
        elite_idx = np.argsort(old_fit)[-elite_size:]
        worst_idx = np.argsort(new_fit)[:elite_size]
        for i, e_idx in enumerate(elite_idx):
            new_pop[worst_idx[i]] = old_pop[e_idx]
            new_fit[worst_idx[i]] = old_fit[e_idx]
        return new_pop, new_fit
 
    def evolve_population(self, population: np.ndarray, fitness_values: np.ndarray) -> Tuple[np.ndarray, np.ndarray, List[Tuple[float, int, int]]]:
        selected = self.selection(population, fitness_values)
        crossed = self.crossover(selected)
        mutated = self.mutation(crossed)
        new_fitness, new_details = self.evaluate_population(mutated)
        final_pop, final_fit = self.elitism(population, mutated, fitness_values, new_fitness)
        return final_pop, final_fit, new_details
 
    def run(self) -> Dict:
        population = self.initialize_population()
        fitness_values, details = self.evaluate_population(population)
 
        best_solution = None
        best_fitness = 0
        best_value = 0
        best_weight = 0
        best_fitness_history = []
        avg_fitness_history = []
 
        for _ in range(self.generations):
            population, fitness_values, details = self.evolve_population(population, fitness_values)
 
            gen_best_idx = np.argmax(fitness_values)
            gen_best_fitness = fitness_values[gen_best_idx]
            gen_best_value = details[gen_best_idx][1]
            gen_best_weight = details[gen_best_idx][2]
 
            best_fitness_history.append(gen_best_fitness)
            avg_fitness_history.append(np.mean(fitness_values))
 
            if gen_best_fitness > best_fitness:
                best_fitness = gen_best_fitness
                best_solution = population[gen_best_idx].copy()
                best_value = gen_best_value
                best_weight = gen_best_weight
 
        selected_items = [i for i, bit in enumerate(best_solution) if bit == 1]
 
        return {
            "solution": best_solution,
            "selected_items": selected_items,
            "total_value": best_value,
            "total_weight": best_weight,
            "capacity": self.capacity,
            "generations": self.generations,
            "best_fitness_history": best_fitness_history,
            "avg_fitness_history": avg_fitness_history,
        }
 
    def plot_progress(self, best_fitness_history: List[float], avg_fitness_history: List[float]) -> None:
        import matplotlib.pyplot as plt
        plt.figure(figsize=(10, 6))
        plt.plot(best_fitness_history, label='Melhor Fitness')
        plt.plot(avg_fitness_history, label='Fitness Médio')
        plt.xlabel('Geração')
        plt.ylabel('Fitness')
        plt.title('Evolução do Fitness ao Longo das Gerações')
        plt.legend()
        plt.grid(True)
        plt.show()
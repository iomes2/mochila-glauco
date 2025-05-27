# test_genetic_knapsack.py

import pytest
import numpy as np
from genetic_knapsack import GeneticKnapsack  # Substitua pelo nome do seu arquivo, sem .py

@pytest.fixture
def knapsack_instance():
    weights = [10, 20, 30]
    values = [60, 100, 120]
    capacity = 50
    return GeneticKnapsack(weights, values, capacity, pop_size=10, generations=5)

def test_population_size(knapsack_instance):
    pop = knapsack_instance.initialize_population()
    assert pop.shape == (10, 3)  # 10 indivíduos, 3 itens

def test_fitness_within_capacity(knapsack_instance):
    solution = np.array([1, 0, 1])  # Peso total: 10 + 30 = 40
    fitness, value, weight = knapsack_instance.fitness(solution)
    assert fitness == 180
    assert weight == 40

def test_fitness_exceeds_capacity(knapsack_instance):
    solution = np.array([1, 1, 1])  # Peso total: 60 (excede 50)
    fitness, value, weight = knapsack_instance.fitness(solution)
    assert fitness == 0  # Penalização
    assert weight == 60

def test_run_returns_expected_keys(knapsack_instance):
    result = knapsack_instance.run()
    expected_keys = {"solution", "selected_items", "total_value", "total_weight", "capacity", "generations", "best_fitness_history", "avg_fitness_history"}
    assert set(result.keys()) == expected_keys

def test_run_solution_size(knapsack_instance):
    result = knapsack_instance.run()
    assert len(result["solution"]) == 3

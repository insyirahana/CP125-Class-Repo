# Lab 01 Exercise 1: Road Trip Budgeter

def is_budget_sufficient (one_way_km,budget):
    total_cost = (one_way_km * 2 / 10) * 2
    return total_cost <= budget

print(is_budget_sufficient(100, 40))
print(is_budget_sufficient(100, 39))

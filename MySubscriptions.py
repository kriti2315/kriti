from itertools import product

def get_newspaper_combinations(budget):
    newspapers = {"TOI": [3, 3, 3, 3, 3, 5, 6], 
                  "Hindu": [2.5, 2.5, 2.5, 2.5, 2.5, 4, 4],
                  "ET": [4, 4, 4, 4, 4, 4, 10],
                  "BM": [1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5],
                  "HT": [2, 2, 2, 2, 2, 4, 4]}
    
    # generate all possible combinations of newspapers
    combinations = [combination for length in range(1, len(newspapers)+1)
                    for combination in product(newspapers, repeat=length)]
    
    # flatten the combinations
    combinations = [{k: v for sub_combination in combinations}]
    
    valid_combinations = []
    for combination in combinations:
        total_cost = sum([sum(subscription) for subscription in combination.values()])
        if total_cost <= budget:
            valid_combinations.append(combination)
    return valid_combinations

weekly_budget = float(input("Enter the weekly budget for subscriptions: "))
combinations = get_newspaper_combinations(weekly_budget)
for combination in combinations:
    print(combination)

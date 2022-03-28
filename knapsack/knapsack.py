"""
    Knapsack exercise
"""
def maximum_value(maximum_weight, items):
    """
        Find the best solution for the knapsack problem
    """
    _dp = [0 for i in range(maximum_weight + 1)]
    chosen_items = [[] for i in range(maximum_weight + 1)]
    for i in range(maximum_weight):
        for index, item in enumerate(items):
            if index not in chosen_items[i]:
                if i + item["weight"] <= maximum_weight:
                    if _dp[i] + item["value"] > _dp[i + item["weight"]]:
                        _dp[i + item["weight"]] = _dp[i] + item["value"]
                        chosen_items[i + item["weight"]] = chosen_items[i] + [index]
    return max(_dp)

"""
    Change exercise
"""
def find_fewest_coins(coins, target):
    """
        Find the solution to return fewest coins with sum = target
    """
    if target < 0:
        raise ValueError("target can't be negative")
    _dp = [target + 1 for i in range(target + 1)]
    solution = [[] for i in range(target + 1)]
    _dp[0] = 0
    for i in range(target):
        for item in coins:
            if i + item <= target and _dp[i + item] > _dp[i] + 1:
                _dp[i + item] = _dp[i] + 1
                solution[i + item] = solution[i] + [item]
    if _dp[target] == target + 1:
        raise ValueError("can't make target with given coins")
    return solution[target]

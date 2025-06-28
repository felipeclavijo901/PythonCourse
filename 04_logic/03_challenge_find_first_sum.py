"""
Dado un array de números y un número goal, encuentra los dos primeros números del array que sumen el número goal y devuelve sus índices. Si no existe tal combinación, devuelve None.

nums = [4, 5, 6, 2]
goal = 8

find_first_sum(nums, goal)  # [2, 3]
"""

def check_first_sum(goal, nums):
    seens = {}
    for idx, n in enumerate(nums):
        complement = goal - n
        if complement in seens:
            return (seens[complement], idx)
        seens[n] = idx

nums = [1, 4, 3, 4, 7, 5, 6, 2]
goal = 8
print(check_first_sum(goal, nums))
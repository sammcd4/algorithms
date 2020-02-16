# Given a number of steps to scale and
# a set of steps that can be taken at once,
# write a function that returns the number of ways to scale the staircase

# Assumptions:
# 1. We can only step up the staircase (creating a finite set of ways to get up the staircase)
#   Otherwise, we could step forward and backward infinitely
# 2. Can use a step counter multiple times i.e. {1, 2} -> 1, 1, 1 to scale 3 steps

# Examples
# N = 4
# steps = {1, 2}
# ways is 5: [[1, 1, 1, 1], [1, 2, 1], [1, 1, 2], [2, 1, 1], [2, 2]]

# N = 2
# steps = {1, 2}
# ways is 2: [[1, 1], [2]]


# brute force method using recursion
def num_ways_to_scale_staircase(N, steps):
    sum_ways = 0
    for step in steps:
        if step == 0:
            continue
        elif step == N:
            sum_ways += 1
        elif step < N:
            sum_ways += num_ways_to_scale_staircase(N-step, steps)

    # account for edge case where scaling a zero-step staircase
    if 0 in steps and sum_ways == 0:
        sum_ways = 1
    return sum_ways

N = 4
steps = {1, 0, 2}
solution = num_ways_to_scale_staircase(N, steps)
print(f'N: {N}, steps: {steps}, solution: {solution}')

print(num_ways_to_scale_staircase(0, steps) == 1)
print(num_ways_to_scale_staircase(1, steps) == 1)
print(num_ways_to_scale_staircase(2, steps) == 2)
print(num_ways_to_scale_staircase(3, steps) == 3)
print(num_ways_to_scale_staircase(4, steps) == 5)
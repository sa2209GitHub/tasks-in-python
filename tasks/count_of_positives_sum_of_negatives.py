'''
    Task:
        Count of Positives
        & Sum of Negatives
'''

# Variables
numbers_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]    # [10, -65];
numbers_2 = [0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14]         # [8, -50];
numbers_3 = None                                                        # []
numbers_4 = []                                                           # []

# First solution
def count_positives_sum_negatives(numbers):
    if not numbers: return []

    count_positives = 0
    sum_negatives = 0

    for number in numbers:
        if number > 0: count_positives += 1
        if number < 0: sum_negatives += number

    return [count_positives, sum_negatives]

# Second solution
def fn2_name(args):
    return 0

# Output
print(count_positives_sum_negatives(numbers_1))
print(count_positives_sum_negatives(numbers_2))
print(count_positives_sum_negatives(numbers_3))
print(count_positives_sum_negatives(numbers_4))

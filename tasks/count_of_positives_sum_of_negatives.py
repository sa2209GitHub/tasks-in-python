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
    if numbers == None or len(numbers) == 0: return []

    answer = [0, 0]

    for number in numbers:
        if number > 0: answer[0] += 1
        if number < 0: answer[1] += number

    return answer

# Second solution
def fn2_name(args):
    return 0

# Output
print(count_positives_sum_negatives(numbers_1))
print(count_positives_sum_negatives(numbers_2))
print(count_positives_sum_negatives(numbers_3))
print(count_positives_sum_negatives(numbers_4))

'''
    Task:
        Sum of Positive
'''

# Variables
numbers_1 = [-1, -2, 0]                 # 0
numbers_2 = [10, 20, 0, -10]            # 30
numbers_3 = [33, -16, 2, 2, 2, -2]      # 39
numbers_4 = [8, 8, 8, 8, 8, 8]          # 48
numbers_5 = [447, 22, 0, 9]             # 478
numbers_6 = [-300, 20, 20, 0, 12]       # 52
numbers_7 = [-1, -1, -1, -1, -1, 0]     # 0
numbers_8 = [-20, 7, 7, 7, 0]           # 21
numbers_9 = [78, 43, 21, 12, 7, 0, -4]  # 161


# Solution
def sum_of_positive(numbers):
    return sum(n for n in numbers if n > 0)

# Output
print(sum_of_positive(numbers_1))
print(sum_of_positive(numbers_2))
print(sum_of_positive(numbers_3))
print(sum_of_positive(numbers_4))
print(sum_of_positive(numbers_5))
print(sum_of_positive(numbers_6))
print(sum_of_positive(numbers_7))
print(sum_of_positive(numbers_8))
print(sum_of_positive(numbers_9))

'''
    Task:
        For Twins: 2
        Math Operations
'''

# Variables
params_1 = [1, 10, 2]    # 16
params_2 = [5, 30, 7]    # 1150

# Solution
def ice_brick_volume(params):
    radius, bottle_length, rim_length = params

    return radius * radius * (bottle_length - rim_length) * 2;

# Output
print(ice_brick_volume(params_1))
print(ice_brick_volume(params_2))

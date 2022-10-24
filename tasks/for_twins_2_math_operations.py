'''
    Task:
        For Twins: 2
        Math Operations
'''

# Variables
params1 = [1, 10, 2]    # 16
params2 = [5, 30, 7]    # 1150

# First solution
def iceBrickVolume(params):
    radius, bottleLength, rimLength = params

    return radius * radius * (bottleLength - rimLength) * 2;

# Output
print(iceBrickVolume(params1))
print(iceBrickVolume(params2))

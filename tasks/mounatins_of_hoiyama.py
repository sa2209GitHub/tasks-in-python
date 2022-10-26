'''
    Task:
        Mountains of Hoiyama
'''

# Variables
peak_1 = 1      # 1
peak_2 = 3      # 7
peak_3 = 5      # 24
peak_4 = 7      # 58
peak_5 = 9      # 115
peak_6 = 11     # 201
peak_7 = 13     # 322
peak_8 = 15     # 484
peak_9 = 17     # 693
peak_10 = 19    # 955

# Solution
def get_mountain_weight(peak):
    weight = 0
    divergence = 0

    for level in range(peak, int(peak / 2), -1):
        weight += level

        for width in range(level - 1, level - divergence - 1, -1):
            weight += width * 2

        divergence += 1;
    
    return weight

# Output
print(get_mountain_weight(peak_1))
print(get_mountain_weight(peak_2))
print(get_mountain_weight(peak_3))
print(get_mountain_weight(peak_4))
print(get_mountain_weight(peak_5))
print(get_mountain_weight(peak_6))
print(get_mountain_weight(peak_7))
print(get_mountain_weight(peak_8))
print(get_mountain_weight(peak_9))
print(get_mountain_weight(peak_10))
